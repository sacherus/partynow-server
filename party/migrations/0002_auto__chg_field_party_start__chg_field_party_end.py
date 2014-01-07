# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Party.start'
        db.alter_column(u'party_party', 'start', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Party.end'
        db.alter_column(u'party_party', 'end', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Party.start'
        db.alter_column(u'party_party', 'start', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 7, 0, 0)))

        # Changing field 'Party.end'
        db.alter_column(u'party_party', 'end', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 7, 0, 0)))

    models = {
        u'party.party': {
            'Meta': {'object_name': 'Party'},
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['party']