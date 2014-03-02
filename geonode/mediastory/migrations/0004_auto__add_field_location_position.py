# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.position'
        db.add_column(u'mediastory_location', 'position',
                      self.gf('geoposition.fields.GeopositionField')(default='0,0', max_length=42),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.position'
        db.delete_column(u'mediastory_location', 'position')


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
            'position': ('geoposition.fields.GeopositionField', [], {'default': "'0,0'", 'max_length': '42'})
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