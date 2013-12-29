# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Party.start'
        db.add_column(u'party_party', 'start',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 29, 0, 0)),
                      keep_default=False)

        # Adding field 'Party.end'
        db.add_column(u'party_party', 'end',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 12, 29, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Party.start'
        db.delete_column(u'party_party', 'start')

        # Deleting field 'Party.end'
        db.delete_column(u'party_party', 'end')


    models = {
        u'party.party': {
            'Meta': {'object_name': 'Party'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['party']