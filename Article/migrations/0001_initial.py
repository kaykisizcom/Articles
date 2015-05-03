# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'Article_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Area'])

        # Adding model 'Cities'
        db.create_table(u'Article_cities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=15)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Article.Area'], null=True, blank=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Cities'])

        # Adding model 'Counties'
        db.create_table(u'Article_counties', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Article.Cities'])),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Counties'])

        # Adding model 'Users'
        db.create_table(u'Article_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('profile_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=11, null=True, blank=True)),
            ('iban', self.gf('django.db.models.fields.CharField')(default='', max_length=34, null=True, blank=True)),
            ('profession', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True)),
            ('account_holder', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=8, decimal_places=2)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Article.Counties'], null=True, blank=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Users'])

        # Adding model 'Message'
        db.create_table(u'Article_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sender', to=orm['auth.User'])),
            ('to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=180)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Message'])

        # Adding model 'MessageContent'
        db.create_table(u'Article_messagecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Message', to=orm['Article.Message'])),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['MessageContent'])

        # Adding model 'AccountProcess'
        db.create_table(u'Article_accountprocess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=180, null=True, blank=True)),
            ('was_paid_price', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=8, decimal_places=2)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['AccountProcess'])

        # Adding model 'ArticleType'
        db.create_table(u'Article_articletype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=180, null=True, blank=True)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['ArticleType'])

        # Adding model 'Article'
        db.create_table(u'Article_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=180, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=180, null=True, blank=True)),
            ('key_word', self.gf('django.db.models.fields.CharField')(default='', max_length=500, null=True, blank=True)),
            ('word_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=8, decimal_places=2)),
            ('is_urgent', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_finished', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('article_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Article.ArticleType'], null=True, blank=True)),
            ('was_paid_price', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=8, decimal_places=2)),
            ('cdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Article', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'Article_area')

        # Deleting model 'Cities'
        db.delete_table(u'Article_cities')

        # Deleting model 'Counties'
        db.delete_table(u'Article_counties')

        # Deleting model 'Users'
        db.delete_table(u'Article_users')

        # Deleting model 'Message'
        db.delete_table(u'Article_message')

        # Deleting model 'MessageContent'
        db.delete_table(u'Article_messagecontent')

        # Deleting model 'AccountProcess'
        db.delete_table(u'Article_accountprocess')

        # Deleting model 'ArticleType'
        db.delete_table(u'Article_articletype')

        # Deleting model 'Article'
        db.delete_table(u'Article_article')


    models = {
        u'Article.accountprocess': {
            'Meta': {'object_name': 'AccountProcess'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '180', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'was_paid_price': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '8', 'decimal_places': '2'})
        },
        u'Article.area': {
            'Meta': {'object_name': 'Area'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'})
        },
        u'Article.article': {
            'Meta': {'object_name': 'Article'},
            'article_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Article.ArticleType']", 'null': 'True', 'blank': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '180', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_urgent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'key_word': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '8', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '180', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'blank': 'True'}),
            'was_paid_price': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '8', 'decimal_places': '2'}),
            'word_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'})
        },
        u'Article.articletype': {
            'Meta': {'object_name': 'ArticleType'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '180', 'null': 'True', 'blank': 'True'})
        },
        u'Article.cities': {
            'Meta': {'object_name': 'Cities'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Article.Area']", 'null': 'True', 'blank': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15'})
        },
        u'Article.counties': {
            'Meta': {'object_name': 'Counties'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Article.Cities']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'})
        },
        u'Article.message': {
            'Meta': {'object_name': 'Message'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sender'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '180'}),
            'to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': u"orm['auth.User']"})
        },
        u'Article.messagecontent': {
            'Meta': {'object_name': 'MessageContent'},
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Message'", 'to': u"orm['Article.Message']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        },
        u'Article.users': {
            'Meta': {'object_name': 'Users'},
            'account_holder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '1', 'max_digits': '8', 'decimal_places': '2'}),
            'birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'cdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Article.Counties']", 'null': 'True', 'blank': 'True'}),
            'iban': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '34', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Article']