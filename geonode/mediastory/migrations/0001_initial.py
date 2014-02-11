# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'mediastory_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mediastory', ['Location'])

        # Adding model 'MediaItem'
        db.create_table(u'mediastory_mediaitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_mediastory.mediaitem_set', null=True, to=orm['contenttypes.ContentType'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mediastory.Location'])),
        ))
        db.send_create_signal(u'mediastory', ['MediaItem'])

        # Adding model 'TextMediaItem'
        db.create_table(u'mediastory_textmediaitem', (
            (u'mediaitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mediastory.MediaItem'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mediastory', ['TextMediaItem'])

        # Adding model 'ImageMediaItem'
        db.create_table(u'mediastory_imagemediaitem', (
            (u'mediaitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mediastory.MediaItem'], unique=True, primary_key=True)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'mediastory', ['ImageMediaItem'])

        # Adding model 'ExternalVideoMediaItem'
        db.create_table(u'mediastory_externalvideomediaitem', (
            (u'mediaitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mediastory.MediaItem'], unique=True, primary_key=True)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
        ))
        db.send_create_signal(u'mediastory', ['ExternalVideoMediaItem'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'mediastory_location')

        # Deleting model 'MediaItem'
        db.delete_table(u'mediastory_mediaitem')

        # Deleting model 'TextMediaItem'
        db.delete_table(u'mediastory_textmediaitem')

        # Deleting model 'ImageMediaItem'
        db.delete_table(u'mediastory_imagemediaitem')

        # Deleting model 'ExternalVideoMediaItem'
        db.delete_table(u'mediastory_externalvideomediaitem')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mediastory.externalvideomediaitem': {
            'Meta': {'object_name': 'ExternalVideoMediaItem', '_ormbases': [u'mediastory.MediaItem']},
            u'mediaitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mediastory.MediaItem']", 'unique': 'True', 'primary_key': 'True'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        },
        u'mediastory.imagemediaitem': {
            'Meta': {'object_name': 'ImageMediaItem', '_ormbases': [u'mediastory.MediaItem']},
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            u'mediaitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mediastory.MediaItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'mediastory.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {})
        },
        u'mediastory.mediaitem': {
            'Meta': {'object_name': 'MediaItem'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mediastory.Location']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_mediastory.mediaitem_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mediastory.textmediaitem': {
            'Meta': {'object_name': 'TextMediaItem', '_ormbases': [u'mediastory.MediaItem']},
            u'mediaitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mediastory.MediaItem']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mediastory']