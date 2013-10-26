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
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('short_text', self.gf('django.db.models.fields.TextField')()),
            ('detail_text', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Page'])

        # Adding model 'Block'
        db.create_table(u'core_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Block'])

        # Adding M2M table for field pages on 'Block'
        m2m_table_name = db.shorten_name(u'core_block_pages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('block', models.ForeignKey(orm['core.block'], null=False)),
            ('page', models.ForeignKey(orm['core.page'], null=False))
        ))
        db.create_unique(m2m_table_name, ['block_id', 'page_id'])

        # Adding model 'Menu'
        db.create_table(u'core_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['Menu'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'core_page')

        # Deleting model 'Block'
        db.delete_table(u'core_block')

        # Removing M2M table for field pages on 'Block'
        db.delete_table(db.shorten_name(u'core_block_pages'))

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
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail_text': ('django.db.models.fields.TextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']