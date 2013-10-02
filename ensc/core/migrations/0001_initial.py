# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'core_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('human_redable_text', self.gf('django.db.models.fields.TextField')()),
            ('seo_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Page'])

        # Adding model 'Block'
        db.create_table(u'core_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('short_text', self.gf('django.db.models.fields.TextField')()),
            ('detail_text', self.gf('django.db.models.fields.TextField')()),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Page'])),
        ))
        db.send_create_signal('core', ['Block'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'core_page')

        # Deleting model 'Block'
        db.delete_table(u'core_block')


    models = {
        'core.block': {
            'Meta': {'object_name': 'Block'},
            'detail_text': ('django.db.models.fields.TextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Page']"}),
            'short_text': ('django.db.models.fields.TextField', [], {})
        },
        'core.page': {
            'Meta': {'object_name': 'Page'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'human_redable_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seo_text': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']