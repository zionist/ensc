# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'core_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Menu'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'core_menu')


    models = {
        'core.block': {
            'Meta': {'ordering': "['-weight']", 'object_name': 'Block'},
            'header': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Page']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.menu': {
            'Meta': {'ordering': "['-weight']", 'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'core.page': {
            'Meta': {'object_name': 'Page'},
            'detail_text': ('django.db.models.fields.TextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']