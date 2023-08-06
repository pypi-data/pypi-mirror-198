from __future__ import print_function

import datetime
import re

from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from markupsafe import Markup
from micawber import parse_html
from peewee import TextField, CharField, SQL, BooleanField, DateTimeField
from playhouse.sqlite_ext import FTSModel

from mblog.config import DATABASE_NEEDS_FTS, flaskDB, database, app, oembedProviders


class Entry(flaskDB.Model):
    title = CharField()
    slug = CharField(unique=True)
    content = TextField()
    published = BooleanField(index=True)
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)

    @property
    def html_content(self):
        """
        Generate HTML representation of the markdown-formatted blog entry,
        and also convert any media URLs into rich media objects such as video
        players or images.
        """
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(self.content, extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembedProviders,
            urlize_all=True,
            maxwidth=app.config['SITE_WIDTH'])
        return Markup(oembed_content)

    def save(self, *args, **kwargs):
        # Generate a URL-friendly representation of the entry's title.
        if not self.slug:
            self.slug = re.sub(r'[^\w]+', '-', self.title.lower()).strip('-')
        ret = super(Entry, self).save(*args, **kwargs)

        # Store search content.
        self.update_search_index()
        return ret

    def update_search_index(self):
        # Create a row in the FTSEntry table with the post content. This will
        # allow us to use SQLite's awesome full-text search extension to
        # search our entries.
        if not DATABASE_NEEDS_FTS:
            return
        exists = (FTSEntry
                  .select(FTSEntry.docid)
                  .where(FTSEntry.docid == self.id)
                  .exists())
        content = '\n'.join((self.title, self.content))
        if exists:
            (FTSEntry
             .update({FTSEntry.content: content})
             .where(FTSEntry.docid == self.id)
             .execute())
        else:
            FTSEntry.insert({
                FTSEntry.docid: self.id,
                FTSEntry.content: content}).execute()

    @classmethod
    def public(cls):
        return Entry.select().where(Entry.published)

    @classmethod
    def drafts(cls):
        return Entry.select().where(not Entry.published)

    @classmethod
    def search(cls, query):
        words = [word.strip() for word in query.split() if word.strip()]
        if not words:
            # Return an empty query.
            return Entry.noop()
        else:
            search = ' '.join(words)

        # Query the full-text search index for entries matching the given
        # search query, then join the actual Entry data on the matching
        # search result.
        if DATABASE_NEEDS_FTS:
            return (Entry
                    .select(Entry, FTSEntry.rank().alias('score'))
                    .join(FTSEntry, on=(Entry.id == FTSEntry.docid))
                    .where(
                FTSEntry.match(search) &
                Entry.published)
                    .order_by(SQL('score')))
        return (Entry
                .select(Entry)
                .where((Entry.content.contains(search)) | (Entry.title.contains(search))))


if DATABASE_NEEDS_FTS:
    class FTSEntry(FTSModel):
        content = TextField()

        class Meta(object):
            database = database


def createDatabases():
    database.create_tables([Entry], safe=True)
    if DATABASE_NEEDS_FTS:
        database.create_tables([FTSEntry], safe=True)

