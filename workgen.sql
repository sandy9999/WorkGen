-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: workgen
-- ------------------------------------------------------
-- Server version	5.7.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add mcq options',7,'add_mcqoptions'),(26,'Can change mcq options',7,'change_mcqoptions'),(27,'Can delete mcq options',7,'delete_mcqoptions'),(28,'Can view mcq options',7,'view_mcqoptions'),(29,'Can add mentor',8,'add_mentor'),(30,'Can change mentor',8,'change_mentor'),(31,'Can delete mentor',8,'delete_mentor'),(32,'Can view mentor',8,'view_mentor'),(33,'Can add questions',9,'add_questions'),(34,'Can change questions',9,'change_questions'),(35,'Can delete questions',9,'delete_questions'),(36,'Can view questions',9,'view_questions'),(37,'Can add subject split',10,'add_subjectsplit'),(38,'Can change subject split',10,'change_subjectsplit'),(39,'Can delete subject split',10,'delete_subjectsplit'),(40,'Can view subject split',10,'view_subjectsplit'),(41,'Can add subject',11,'add_subject'),(42,'Can change subject',11,'change_subject'),(43,'Can delete subject',11,'delete_subject'),(44,'Can view subject',11,'view_subject'),(45,'Can add chapter',12,'add_chapter'),(46,'Can change chapter',12,'change_chapter'),(47,'Can delete chapter',12,'delete_chapter'),(48,'Can view chapter',12,'view_chapter'),(49,'Can add generated test and generic paper',13,'add_generatedtestandgenericpaper'),(50,'Can change generated test and generic paper',13,'change_generatedtestandgenericpaper'),(51,'Can delete generated test and generic paper',13,'delete_generatedtestandgenericpaper'),(52,'Can view generated test and generic paper',13,'view_generatedtestandgenericpaper'),(53,'Can add generated customized paper',14,'add_generatedcustomizedpaper'),(54,'Can change generated customized paper',14,'change_generatedcustomizedpaper'),(55,'Can delete generated customized paper',14,'delete_generatedcustomizedpaper'),(56,'Can view generated customized paper',14,'view_generatedcustomizedpaper');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$9nm4ZeW7QDqi$SpnKHmevOPGrXiB4AzVuN06/q55wHq6YaE+YJSQidWY=','2019-08-12 04:18:53.336634',1,'pai','','','',1,1,'2019-08-12 04:18:37.917863');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-08-12 04:20:45.314897','1','pai',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(12,'searchapp','chapter'),(14,'searchapp','generatedcustomizedpaper'),(13,'searchapp','generatedtestandgenericpaper'),(7,'searchapp','mcqoptions'),(8,'searchapp','mentor'),(9,'searchapp','questions'),(11,'searchapp','subject'),(10,'searchapp','subjectsplit'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-12 04:16:09.753791'),(2,'auth','0001_initial','2019-08-12 04:16:20.859417'),(3,'admin','0001_initial','2019-08-12 04:16:23.424994'),(4,'admin','0002_logentry_remove_auto_add','2019-08-12 04:16:23.473679'),(5,'admin','0003_logentry_add_action_flag_choices','2019-08-12 04:16:23.517242'),(6,'contenttypes','0002_remove_content_type_name','2019-08-12 04:16:24.685825'),(7,'auth','0002_alter_permission_name_max_length','2019-08-12 04:16:25.435562'),(8,'auth','0003_alter_user_email_max_length','2019-08-12 04:16:26.528829'),(9,'auth','0004_alter_user_username_opts','2019-08-12 04:16:26.581693'),(10,'auth','0005_alter_user_last_login_null','2019-08-12 04:16:27.541402'),(11,'auth','0006_require_contenttypes_0002','2019-08-12 04:16:27.575327'),(12,'auth','0007_alter_validators_add_error_messages','2019-08-12 04:16:27.622443'),(13,'auth','0008_alter_user_username_max_length','2019-08-12 04:16:28.581599'),(14,'auth','0009_alter_user_last_name_max_length','2019-08-12 04:16:29.351245'),(15,'searchapp','0001_initial','2019-08-12 04:16:32.779426'),(16,'searchapp','0002_auto_20180809_1101','2019-08-12 04:16:34.055320'),(17,'searchapp','0003_auto_20180813_1345','2019-08-12 04:16:34.500670'),(18,'searchapp','0004_questions_chapter_number','2019-08-12 04:16:35.359378'),(19,'searchapp','0005_questions_source','2019-08-12 04:16:35.942746'),(20,'searchapp','0006_auto_20180822_0923','2019-08-12 04:16:38.566530'),(21,'searchapp','0007_auto_20180822_1603','2019-08-12 04:16:40.062185'),(22,'searchapp','0008_auto_20180823_1537','2019-08-12 04:16:40.710765'),(23,'searchapp','0009_generatedquestionpaper_submitted_date','2019-08-12 04:16:41.501596'),(24,'searchapp','0010_subjectsplit_subject','2019-08-12 04:16:43.053452'),(25,'searchapp','0011_auto_20180919_0759','2019-08-12 04:16:49.138645'),(26,'searchapp','0012_auto_20181215_2236','2019-08-12 04:16:49.758120'),(27,'sessions','0001_initial','2019-08-12 04:16:50.398364');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('nailhe04k86re6ts54d14yu5shr3lkln','ZThlOWExODI0NTk1YzY4ZWY3NmMyMTBhNzcwNGUxNzU0MzJkMzdiMjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwNzgxYjExYTlhMjRlN2UyMGNkZmY2MTRhYzU3YTk5NWQwYjNhNjIxIn0=','2019-08-26 04:18:53.390559');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_chapter`
--

DROP TABLE IF EXISTS `searchapp_chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_chapter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chapter_name` varchar(100) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `searchapp_chapter_subject_id_80448fd4_fk_searchapp_subject_id` (`subject_id`),
  CONSTRAINT `searchapp_chapter_subject_id_80448fd4_fk_searchapp_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `searchapp_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_chapter`
--

LOCK TABLES `searchapp_chapter` WRITE;
/*!40000 ALTER TABLE `searchapp_chapter` DISABLE KEYS */;
INSERT INTO `searchapp_chapter` VALUES (1,'Periodic Classification of Elements',1),(2,'Chemical Reaction and Equations',1),(3,'Effects of electric current',1),(4,'Heat',1),(5,'Refraction of Light',1),(6,'Lenses',1),(7,'Metallurgy',1),(8,'Carbon Compounds',1),(9,'Space Missions',1),(10,'Gravitation',1);
/*!40000 ALTER TABLE `searchapp_chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_generatedcustomizedpaper`
--

DROP TABLE IF EXISTS `searchapp_generatedcustomizedpaper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_generatedcustomizedpaper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(100) NOT NULL,
  `file_path` varchar(200) DEFAULT NULL,
  `is_ready` tinyint(1) NOT NULL,
  `mentor_id` int(11) NOT NULL,
  `submitted_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `searchapp_generatedq_mentor_id_b04a7960_fk_auth_user` (`mentor_id`),
  CONSTRAINT `searchapp_generatedq_mentor_id_b04a7960_fk_auth_user` FOREIGN KEY (`mentor_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_generatedcustomizedpaper`
--

LOCK TABLES `searchapp_generatedcustomizedpaper` WRITE;
/*!40000 ALTER TABLE `searchapp_generatedcustomizedpaper` DISABLE KEYS */;
/*!40000 ALTER TABLE `searchapp_generatedcustomizedpaper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_generatedtestandgenericpaper`
--

DROP TABLE IF EXISTS `searchapp_generatedtestandgenericpaper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_generatedtestandgenericpaper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(100) NOT NULL,
  `file_path` varchar(200) DEFAULT NULL,
  `is_ready` tinyint(1) NOT NULL,
  `submitted_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_generatedtestandgenericpaper`
--

LOCK TABLES `searchapp_generatedtestandgenericpaper` WRITE;
/*!40000 ALTER TABLE `searchapp_generatedtestandgenericpaper` DISABLE KEYS */;
/*!40000 ALTER TABLE `searchapp_generatedtestandgenericpaper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_mcqoptions`
--

DROP TABLE IF EXISTS `searchapp_mcqoptions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_mcqoptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `option_value` varchar(100) NOT NULL,
  `question_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `searchapp_mcqoptions_question_id_id_c16ec340_fk_searchapp` (`question_id_id`),
  CONSTRAINT `searchapp_mcqoptions_question_id_id_c16ec340_fk_searchapp` FOREIGN KEY (`question_id_id`) REFERENCES `searchapp_questions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_mcqoptions`
--

LOCK TABLES `searchapp_mcqoptions` WRITE;
/*!40000 ALTER TABLE `searchapp_mcqoptions` DISABLE KEYS */;
/*!40000 ALTER TABLE `searchapp_mcqoptions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_mentor`
--

DROP TABLE IF EXISTS `searchapp_mentor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_mentor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `phone` varchar(40) DEFAULT NULL,
  `email` varchar(40) NOT NULL,
  `mentor_type` int(11) NOT NULL,
  `full_name` varchar(40) NOT NULL,
  `created_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_mentor`
--

LOCK TABLES `searchapp_mentor` WRITE;
/*!40000 ALTER TABLE `searchapp_mentor` DISABLE KEYS */;
INSERT INTO `searchapp_mentor` VALUES (1,'pai','pbkdf2_sha256$120000$9nm4ZeW7QDqi$SpnKHm',NULL,'paiakshay998@gmail.com',2,'Akshay Pai','2019-08-12 04:20:45.312361');
/*!40000 ALTER TABLE `searchapp_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_questions`
--

DROP TABLE IF EXISTS `searchapp_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chapter_id` int(11) DEFAULT NULL,
  `question_weightage` int(11) DEFAULT NULL,
  `text` longtext NOT NULL,
  `uploaded_by_id` int(11) NOT NULL,
  `question_type` int(11) DEFAULT NULL,
  `source` longtext,
  PRIMARY KEY (`id`),
  KEY `searchapp_questions_uploaded_by_id_1cfb802f_fk_searchapp` (`uploaded_by_id`),
  KEY `searchapp_questions_chapter_id_456662ae` (`chapter_id`),
  CONSTRAINT `searchapp_questions_chapter_id_456662ae_fk_searchapp_chapter_id` FOREIGN KEY (`chapter_id`) REFERENCES `searchapp_chapter` (`id`),
  CONSTRAINT `searchapp_questions_uploaded_by_id_1cfb802f_fk_searchapp` FOREIGN KEY (`uploaded_by_id`) REFERENCES `searchapp_mentor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_questions`
--

LOCK TABLES `searchapp_questions` WRITE;
/*!40000 ALTER TABLE `searchapp_questions` DISABLE KEYS */;
INSERT INTO `searchapp_questions` VALUES (1,10,1,'Explain why the value of g is zero at the centre of the earth?',1,2,NULL),(2,10,1,'An object takes 5 s to reach the grond from a height of 5 m on a planet. What is the value of g on the planet?',1,2,NULL),(3,10,1,'The radius of planet A is half the radius of planet B. If the mass of A is MA, what must be the mass of B so that the value of g on B is half that of its value on A?',1,2,NULL),(4,10,1,'The mass and weight of an object on earth are 5 kg and 49 N respectively. What will be their values on the moon? Assume that the acceleration due to gravity on the moon is 1/6th of that on the earth.',1,2,NULL),(5,10,1,'What is the difference between mass and weight of an object. Will the mass and weight of an object on the earth be same as their values on Mars? Why?',1,3,NULL),(6,10,1,'What are (i) free fall, (ii) acceleration due to gravity (iii) escape velocity (iv) centripetal force ?',1,3,NULL),(7,10,1,'A stone thrown vertically upwards with initial velocity u reaches a height ‘h’ before coming down. Show that the time taken to go up is same as the time taken to come down.',1,3,NULL),(8,10,1,'If the value of g suddenly becomes twice its value, it will become two times more difficult to pull a heavy object along the floor. Why?',1,3,NULL),(9,10,1,'Let the period of revolution of a planet at a distance R from a star be T. Prove that if it was at a distance of 2R from the star, its period of revolution will be 8 T.',1,3,NULL),(10,10,1,'A ball falls off a table and reaches the ground in 1 s. Assuming g = 10 m/s2, calculate its speed on reaching the ground and the height of the table.',1,3,NULL),(11,10,1,'The masses of the earth and moon are 6 x 1024 kg and 7.4x1022 kg, respectively. The distance between them is 3.84 x 105 km. Calculate the gravitational force of attraction between the two?',1,3,NULL),(12,10,1,'The mass of the earth is 6 x 1024 kg. The distance between the earth and the Sun is 1.5x 1011 m. If the gravitational force between the two is 3.5 x 1022 N, what is the mass of the Sun?',1,3,NULL),(13,10,1,'Write the three laws given by Kepler. How did they help Newton to arrive at the inverse square law of gravity?',1,5,NULL),(14,1,1,'The number of electrons in the outermost shell of alkali metals is ____________(i)1 (ii) 2 (iii) 3 (iv) 7',1,1,NULL),(15,1,1,'Alkaline earth metals have valency 2. This means that their position in the modern periodic table is in ______(i)Group 2 (ii) Group16 (iii) Period 2 (iv) d-block',1,1,NULL),(16,1,1,'Molecular formula of the chloride of an element X is XCl. This compound is a solid having high melting point. Which of the following elements be present in the same group as X. (i)Na (ii) Mg (iii) Al (iv) Si',1,1,NULL),(17,1,1,'In which block of the modern periodic table are the non-metals found?(i)s-block (ii) p-block (iii) d-block (iv) f-block',1,1,NULL),(18,1,2,'3 Li, 14Si, 2 He, 11Na, 15P - Which of these elements belong to be period 3?',1,1,NULL),(19,1,2,'1H, 7N, 20Ca, 16S, 4Be, 18Ar- Which of these elements belong to the second group?',1,1,NULL),(20,1,2,'7N, 6C, 8O, 5B, 13A1 - Which is the most electronegative element among these?',1,1,NULL),(21,1,2,'4Be, 6C, 8O, 5B, 13A1 - Which is the most electropositive element among these?',1,1,NULL),(22,1,2,'11Na, 15P, 17C1, 14Si, 12Mg - Which of these has largest atoms?',1,1,NULL),(23,1,2,'19K, 3Li, 11Na, 4Be - Which of these atoms has smallest atomic radius?',1,1,NULL),(24,1,2,'13A1, 14Si, 11Na, 12Mg, 16S - Which of the above elements has the highest metallic character?',1,1,NULL),(25,1,2,'6C, 3Li, 9F, 7N, 8O Which of the above elements has the highest non-metallic character?',1,1,NULL),(26,1,2,'Identify the element: The atom having the smallest size.',1,1,NULL),(27,1,2,'Identify the element: The atom having the smallest atomic mass.',1,1,NULL),(28,1,2,'Identify the element: The most electronegative atom.',1,1,NULL),(29,1,2,'Identify the element: The noble gas with the smallest atomic radius.',1,1,NULL),(30,1,2,'Identify the element: The most reactive nonmetal.',1,1,NULL),(31,1,1,'An element has its electron configuration as 2,8,2. What is the atomic number of this element? What is the group of this element? To which period does this element belong? ',1,2,NULL),(32,1,1,'Describe: Mendeleev’s periodic law.',1,2,NULL),(33,1,1,'Describe: Structure of the modern periodic table.',1,2,NULL),(34,1,1,'Describe: Position of isotopes in the Mendeleev’s and the modern periodic table',1,2,NULL),(35,1,1,'Give Reasons: Atomic radius goes on decreasing while going from left to right in a period.',1,2,NULL),(36,1,1,'Give Reasons: Metallic character goes on decreasing while going from left to right in a period.',1,2,NULL),(37,1,1,'Give Reasons: Atomic radius goes on increasing down a group.',1,2,NULL),(38,1,1,'Give Reasons: Elements belonging to the same group have the same valency.',1,2,NULL),(39,1,1,'Give Reasons: The third period contains only eight elements even through the electron capacity of the third shell is 18',1,2,NULL),(40,1,1,'Identify: The period with electrons in the shells K, L and M.',1,2,NULL),(41,1,1,'Identify: The group with valency zero.',1,2,NULL),(42,1,1,'Identify: The family of nonmetals having valency one.',1,2,NULL),(43,1,1,'Identify: The family of metals having valency one.',1,2,NULL),(44,1,1,'Identify: The family of metals having valency two.',1,2,NULL),(45,1,1,'Identify: The metalloids in the second and third periods.',1,2,NULL),(46,1,1,'Identify: Nonmetals in the third period.',1,2,NULL),(47,1,1,'Identify: Two elements having valency 4.',1,2,NULL),(48,2,1,'To prevent rusting, a layer of ........ metal is applied on iron sheets.',1,1,NULL),(49,2,1,'The conversion of ferrous sulphate to ferric sulphate is ........ reaction.',1,1,NULL),(50,2,1,'When electric current is passed through acidulated water ........ of water takes place.',1,1,NULL),(51,2,1,'Addition of an aqueous solution of ZnSO4 to an aqueous solution of BaCl2 is an example of ....... reaction.',1,1,NULL),(52,2,2,'Identify reactants and products undergoing oxidation and reducation: Fe + S → FeS',1,1,NULL),(53,2,2,'Identify reactants and products undergoing oxidation and reducation: 2Ag2 O → 4 Ag + O2 ↑',1,1,NULL),(54,2,2,'Identify reactants and products undergoing oxidation and reducation: 2Mg + O2 → 2MgO',1,1,NULL),(55,2,2,'Identify reactants and products undergoing oxidation and reducation: NiO + H2 → Ni + H2O',1,1,NULL),(56,2,2,'Identify endothermic and exothermic: HCl + NaOH → NaCl + H2O + heat',1,1,NULL),(57,2,2,'Identify endothermic and exothermic: 2KClO3 (s) → 2KCl(s) + 3O2 ↑',1,1,NULL),(58,2,2,'Identify endothermic and exothermic: CaO + H2O → Ca(OH)2 + heat',1,1,NULL),(59,2,2,'Identify endothermic and exothermic: CaCO3 (s) CaO(s) + CO2↑',1,1,NULL),(60,2,1,'What is the reaction called when oxidation and reduction take place simultaneously? Explain with one example.',1,2,NULL),(61,2,1,'How can the rate of the chemical reaction, namely, decomposition of hydrogen peroxide be increased?',1,2,NULL),(62,2,1,'Explain the term reactant and product giving examples.',1,2,NULL),(63,2,1,'Explain the types of reaction with reference to oxygen and hydrogen. Illustratre with examples.',1,2,NULL),(64,2,1,'Explain the similarity and difference in two events, namely adding NaOH to water and adding CaO to water.',1,2,NULL),(65,2,1,'Explain with examples: Endothermic reaction',1,2,NULL),(66,2,1,'Explain with examples: Combination reaction',1,2,NULL),(67,2,1,'Explain with examples: Balanced equation',1,2,NULL),(68,2,1,'Explain with examples: Displacement reaction',1,2,NULL),(69,2,1,'When the gas formed on heating limestone is passed through freshly prepared lime water, the lime water turns milky.',1,2,NULL),(70,2,1,'It takes time for pieces of Shahabad tile to disappear in HCl, but its powder disappears rapidly.',1,2,NULL),(71,2,1,'While preparing dilute sulphuric acid from concentrated sulphuric acid in the laboratory, the concentrated sulphuric acid is added slowly to water with constant stirring.',1,2,NULL),(72,2,1,'It is recommended to use air-tight container for storing oil for long time.',1,2,NULL),(73,2,1,'Balance the reaction: H2 S2 O7 (l) + H2 O(1) → H2SO4 (l)',1,2,NULL),(74,2,1,'Balance the reaction: SO2 (g) + H2S(aq) → S(s) + H2O (l)',1,2,NULL),(75,2,1,'Balance the reaction: Ag(s) + HCl(aq) → AgCl ↓+ H2↑',1,2,NULL),(76,2,1,'Balance the reaction: NaOH (aq) + H2SO4 (aq) → Na2SO4 (aq) + H2O(l)',1,2,NULL),(77,3,2,'Odd one out: Fuse wire, bad conductor, rubber gloves, generator.',1,1,NULL),(78,3,2,'Odd one out: Voltmeter, Ammeter, galvanometer, thermometer.',1,1,NULL),(79,3,2,'Odd one out: Loud speaker, microphone, electric motor, magnet.',1,1,NULL),(80,3,1,'How does the short circuit form? What is its effect?',1,2,NULL),(81,3,1,'Give Scientific reasons: Tungsten metal is used to make a solenoid type coil in an electric bulb.',1,2,NULL),(82,3,1,'Give Scientific reasons: In the electic equipment producing heat e.g. iron, electric heater, boiler, toaster etc, an alloy such as Nichrome is used, not pure metals.',1,2,NULL),(83,3,1,'Give Scientific reasons: For electric power transmission, copper or aluminium wire is used.',1,2,NULL),(84,3,1,'Give Scientific reasons: In practice the unit kWh is used for the measurement of electrical energy, rather than joule.',1,2,NULL),(85,3,1,'Heat energy is being produced in a resistance in a circuit at the rate of 100 W. The current of 3 A is flowing in the circuit. What must be the value of the resistance?',1,2,NULL),(86,3,1,'Explain the construction and working of the following. Draw a neat diagram and label it: Electric motor',1,3,NULL),(87,3,1,'Explain the construction and working of the following. Draw a neat diagram and label it: Electric Generator(AC)',1,3,NULL),(88,3,1,'Explain the difference : AC generator and DC generator',1,3,NULL),(89,3,1,'What is a solenoid? Compare the magnetic field produced by a solenoid with the magnetic field of a bar magnet. Draw neat figures and name various components',1,3,NULL),(90,3,1,'Which device is used to produce electricity? Describe with a neat diagram. Electric motor b. Galvanometer c. Electric Generator (DC) d. Voltmeter',1,3,NULL),(91,3,1,'Two tungsten bulbs of wattage 100 W and 60 W power work on 220 V potential difference. If they are connected in parallel, how much current will flow in the main conductor?',1,3,NULL),(92,3,1,'Who will spend more electrical energy? 500 W TV Set in 30 mins, or 600 W heater in 20 mins?',1,3,NULL),(93,3,1,'An electric iron of 1100 W is operated for 2 hrs daily. What will be the electrical consumption expenses for that in the month of April? (The electric company charges Rs 5 per unit of energy).',1,3,NULL),(94,4,1,'The amount of water vapor in air is determined in terms of its …………',1,1,NULL),(95,4,1,'If objects of equal masses are given equal heat, their final temperature will be different. This is due to difference in their ……………...',1,1,NULL),(96,4,1,'During transformation of liquid phase to solid phase, the latent heat is ………….',1,1,NULL),(97,4,1,'While deciding the unit for heat, which temperatures interval is chosen? Why?',1,2,NULL),(98,4,1,'How can you relate the formation of water droplets on the outer surface of a bottle taken out of refrigerator with formation of dew?',1,2,NULL),(99,4,1,'In cold regions in winter, the rocks crack due to anomalous expansion of water.',1,2,NULL),(100,4,1,'Which principle is used to measure the specific heat capacity of a substance?',1,2,NULL),(101,4,1,'On what basis and how will you determine whether air is saturated with vapor or not?',1,2,NULL),(102,4,1,'Considering the change in volume of water as its temperature is raised from 0 o C, discuss the difference in the behaviour of water and other substances. What is this behaviour of water called?',1,3,NULL),(103,4,1,'What is meant by specific heat capacity? How will you prove experimentally that different substances have different specific heat capacities?',1,3,NULL),(104,4,1,'What is the role of anomalous behaviour of water in preserving aquatic life in regions of cold climate?',1,3,NULL),(105,4,1,'What is meant by latent heat? How will the state of matter transform if latent heat is given off?',1,3,NULL),(106,4,1,'Explain the role of latent heat in the change of state of a substance?',1,3,NULL),(107,4,1,'Equal heat is given to two objects A and B of mass 1 g. Temperature of A increases by 3o C and B by 5o C. Which object has more specific heat? And by what factor? ',1,3,NULL),(108,4,1,'Liquid ammonia is used in ice factory for making ice from water. If water at 20o C is to be converted into 2 kg ice at 0o C, how many grams of ammonia are to be evaporated? (Given: The latent heat of vaporization of ammonia= 341 cal/g)',1,3,NULL),(109,4,1,'A thermally insulated pot has 150 g ice at temperature 0o C. How much steam of 100o C has to be mixed to it, so that water of temperature 50o C will be obtained? (Given : latent heat of melting of ice = 80 cal/g, latent heat of vaporization of water = 540 cal/g, specific heat of water = 1 cal/g0 C) ',1,3,NULL),(110,4,1,'A calorimeter has mass 100 g and specific heat 0.1 kcal/ kg oC. It contains 250 gm of liquid at 30 oC having specific heat of 0.4 kcal/kgo C. If we drop a piece of ice of mass 10 g at 0o C, What will be the temperature of the mixture? (4 marks)',1,5,NULL),(111,5,1,'Refractive index depends on the ............. of light.',1,1,NULL),(112,5,1,'The change in ................ of light rays while going from one medium to another is called refraction.',1,1,NULL),(113,5,1,'We can see the Sun even when it is little below the horizon because of _______  a) Reflection of light  b) Refraction of light   c) Dispersion of light   d) Absorption of light',1,1,NULL),(114,5,1,'If the angle of incidence and angle of emergence of a light ray falling on a glass slab are i and e respectively, prove that, i = e.',1,2,NULL),(115,5,1,'A rainbow is the combined effect of the refraction, dispersion, and total internal reflection of light.',1,2,NULL),(116,5,1,'What is the reason for the twinkling of stars?',1,2,NULL),(117,5,1,'If the speed of light in a medium is 1.5 x 108 m/s, what is the absolute refractive index of the medium?',1,2,NULL),(118,5,1,'If the absolute refractive indices of glass and water are 3/2 and 4/3 respectively, what is the refractive index of glass with respect to water?',1,3,NULL),(119,6,1,'At which position will you keep an object in front of a convex lens so as to get a real image of the same size as the object ? Draw a figure',1,2,NULL),(120,6,1,'Draw a figure explaining various terms related to a lens',1,2,NULL),(121,6,1,'Give Scientific reasons: Simple microscope is used for watch repairs.',1,2,NULL),(122,6,1,'Give Scientific reasons: One can sense colours only in bright light.',1,2,NULL),(123,6,1,'Give Scientific reasons: We can not clearly see an object kept at a distance less than 25 cm from the eye.',1,2,NULL),(124,6,1,'Distinguish Between: Farsightedness and Nearsightedness',1,3,NULL),(125,6,1,'Distinguish Between: Concave lens and Convex Lens',1,3,NULL),(126,6,1,'Doctor has prescribed a lens having power +1.5 D. What will be the focal length of the lens? What is the type of the lens and what must be the defect of vision?',1,3,NULL),(127,6,1,'Three lenses having power 2, 2.5 and 1.7 D are kept touching in a row. What is the total power of the lens combination?( 3marks )',1,3,NULL),(128,6,1,'An object kept 60 cm from a lens gives a virtual image 20 cm in front of the lens. What is the focal length of the lens? Is it a converging lens or diverging lens?',1,3,NULL),(129,6,1,'Explain the working of an astronomical telescope using refraction of light',1,5,NULL),(130,6,1,'What is the function of iris and the muscles connected to the lens in human eye?',1,5,NULL),(131,6,1,'5 cm high object is placed at a distance of 25 cm from a converging lens of focal length of 10 cm. Determine the position, size and type of the image ( 4 marks )',1,5,NULL),(132,7,2,'Write names: Alloy of sodium with mercury.',1,1,NULL),(133,7,2,'Write names: Molecular formula of the common ore of aluminium.',1,1,NULL),(134,7,2,'Write names: The oxide that forms salt and water by reacting with both acid and base.',1,1,NULL),(135,7,2,'Write names: The device used for grinding an ore.',1,1,NULL),(136,7,2,'Write names: The non-metal having electrical conductivity.',1,1,NULL),(137,7,2,'Write names: The reagent that dissolves noble metals.',1,1,NULL),(138,7,1,'Explain the terms. a. Metallurgy b. Ores c. Minerals d. Gangue',1,2,NULL),(139,7,1,'Write scientific reasons: Lemon or tamarind is used for cleaning copper vessels turned greenish.',1,2,NULL),(140,7,1,'Write scientific reasons: Lemon or tamarind is used for cleaning copper vessels turned greenish.Generally the ionic compounds have high melting points.',1,2,NULL),(141,7,1,'Write scientific reasons: Generally the ionic compounds have high melting points.Sodium is always kept in kerosene.',1,2,NULL),(142,7,1,'Write scientific reasons: Generally the ionic compounds have high melting points.Sodium is always kept in kerosene.',1,2,NULL),(143,7,1,'Write scientific reasons: Sodium is always kept in kerosene.',1,2,NULL),(144,7,1,'When a copper coin is dipped in silver nitrate solution, a glitter appears on the coin after some time. Why does this happen? Write the chemical equation.',1,2,NULL),(145,7,1,'Write chemical equations: Aluminium came in contact with air.',1,2,NULL),(146,7,1,'Write chemical equations: Iron filings are dropped in aqueous solution of copper sulphate.',1,2,NULL),(147,7,1,'Write chemical equations: A reaction was brought about between ferric oxide and aluminium.',1,2,NULL),(148,7,1,'Write chemical equations: Electrolysis of alumina is done.',1,2,NULL),(149,7,1,'Write chemical equations: A reaction was brought about between ferric oxide and aluminium.',1,2,NULL),(150,7,1,'Divide the metals Cu, Zn, Ca, Mg, Fe, Na, Li into three groups, namely reactive metals, moderately reactive metals and less reactive metals',1,2,NULL),(151,7,1,'The electronic configuration of metal ‘A’ is 2,8,1 and that of metal ‘B’ is 2,8,2. Which of the two metals is more reactive? Write their reaction with dilute hydrochloric acid',1,3,NULL),(152,7,1,'Draw neat labelled diagram: Magnetic separation method.',1,3,NULL),(153,7,1,'Draw neat labelled diagram: Electrolytic reduction of alumina.',1,3,NULL),(154,7,1,'Draw neat labelled diagram: Froth floatation method.',1,3,NULL),(155,7,1,'Draw neat labelled diagram: Hydraulic separation method.',1,3,NULL),(156,8,1,'Draw an electron dot structure of the following molecules. (Without showing the circles)Methane b. Ethene c. Methanol d. Water',1,2,NULL),(157,8,1,'Explain with an example.Structural isomerism',1,2,NULL),(158,8,1,'Explain with an example.Covalent bond',1,2,NULL),(159,8,1,'Explain with an example.Hetero atom in a carbon compound',1,2,NULL),(160,8,1,'Explain with an example.Functional group',1,2,NULL),(161,8,1,'Explain with an example.Alkane',1,2,NULL),(162,8,1,'Explain with an example.Unsaturated hydrocarbon',1,2,NULL),(163,8,1,'Explain with an example.Homopolymer',1,2,NULL),(164,8,1,'Explain with an example.Monomer',1,2,NULL),(165,8,1,'Explain with an example.Reduction',1,2,NULL),(166,8,1,'Explain with an example.Oxydant',1,2,NULL),(167,8,1,'Write the IUPAC names of the following structural formulae.CH3 -CH2 -CH2 -CH3',1,2,NULL),(168,8,1,'Write the IUPAC names of the following structural formulae.CH3 -CHOH-CH3',1,2,NULL),(169,8,1,'Write the IUPAC names of the following structural formulae.CH3 -CH2 -COOH',1,2,NULL),(170,8,1,'Write the IUPAC names of the following structural formulae.CH3 -CH2 -NH2',1,2,NULL),(171,8,1,'Write the IUPAC names of the following structural formulae.CH3 -CHO',1,2,NULL),(172,8,1,'Identify the reaction: CH3 -CH2 -CH2 -OH → CH3 -CH2 -COOH',1,2,NULL),(173,8,1,'Identify the reaction: CH3 -COOH + CH3 -OH → CH3 -COO- CH3 + H2 O',1,2,NULL),(174,8,1,'Identify the reaction: CH3 -CH2 -CH3 → 3CO2 + 4 H2O',1,2,NULL),(175,8,1,'Identify the reaction: CH3 -CH= CH -CH3 + Br2 → CH3 -CHBr - CHBr -CH3',1,2,NULL),(176,8,1,'Identify the reaction: CH3 -CH3 + Cl2 → CH3 -CH2 -Cl + HCl',1,2,NULL),(177,8,1,'Identify the reaction: CH3 -CH2 -CH2 -CH2 -OH → CH3 -CH2 -CH=CH2 + H2O',1,2,NULL),(178,8,1,'Identify the reaction: CH3 -CH2 -COOH + NaOH → CH3 -CH2 -COONa+ + H2 O',1,2,NULL),(179,8,1,'What causes the existence of very large number of carbon compound',1,2,NULL),(180,8,1,'What is meant by vinegar and gasohol? What are their uses?',1,2,NULL),(181,8,1,'What is a catalyst? Write any one reaction which is brought about by use of catalyst?',1,2,NULL),(182,8,1,'Write structural formula: pent-2-one',1,2,NULL),(183,8,1,'Write structural formula: 2- chlorobutane',1,2,NULL),(184,8,1,'Write structural formula: propan- 2 ol',1,2,NULL),(185,8,1,'Write structural formula: d. methanal',1,2,NULL),(186,8,1,'Write structural formula: butanoic acid',1,2,NULL),(187,8,1,'Write structural formula: 1- bromopropane',1,2,NULL),(188,8,1,'Write structural formula: ethanamine',1,2,NULL),(189,8,1,'Write structural formula: butanone',1,2,NULL),(190,8,1,'Draw all possible structural formulae of compounds from their molecular formula given below.     a. C3 H8      b. C4 H10     c. C3 H4',1,3,NULL),(191,8,1,'Saturated hydrocarbons are classified into three types. Write these names giving one example each.',1,3,NULL),(192,8,1,'Give any four functional groups containing oxygen as the heteroatom in it. Write name and structural formula of one example each.',1,3,NULL),(193,8,1,'Give names of three functional groups containing three different hetero atoms. Write name and structural formula of one example each.',1,3,NULL),(194,8,1,'Give names of three natural polymers. Write the place of their occurrence and names of monomers from which they are formed.',1,3,NULL),(195,9,1,'If the height of the orbit of a satellite from the earth surface is increased, the tangential velocity of the satellite will …',1,1,NULL),(196,9,1,'The initial velocity (during launching) of the Managalyaan, must be greater than …………..of the earth',1,1,NULL),(197,9,2,'True or False: If a spacecraft has to be sent away from the influence of earth’s gravitational field, its velocity must be less than the escape velocity.',1,1,NULL),(198,9,2,'True or False: The escape velocity on the moon is less than that on the earth.',1,1,NULL),(199,9,2,'True or False: A satellite needs a specific velocity to revolve in a specific orbit.',1,1,NULL),(200,9,2,'True or False: If the height of the orbit of a satellite increases, its velocity must also increase.',1,1,NULL),(201,9,1,'What is meant by an artificial satellite? How are the satellites classified based on their functions?',1,2,NULL),(202,9,1,'What is meant by the orbit of a satellite? On what basis and how are the orbits of artificial satellites classified?',1,2,NULL),(203,9,1,'Why are geostationary satellites not useful for studies of polar regions?',1,2,NULL),(204,9,1,'What is meant by satellite launch vehicles? Explain a satellite launch vehicle developed by ISRO with the help of a schematic diagram',1,2,NULL),(205,9,1,'Why it is beneficial to use satellite launch vehicles made of more than one stage?',1,2,NULL),(206,9,1,'If mass of a planet is eight times the mass of the earth and its radius is twice the radius of the earth, what will be the escape velocity for that planet?',1,3,NULL),(207,9,1,'If the height of a satellite completing one revolution around the earth in T seconds is h1 meter, then what would be the height of a satellite taking seconds for one revolution?',1,3,NULL),(208,9,1,'How much time a satellite in an orbit at height 35780 km above earth’s surface would take, if the mass of the earth would have been four times its original mass?',1,3,NULL);
/*!40000 ALTER TABLE `searchapp_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_subject`
--

DROP TABLE IF EXISTS `searchapp_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `searchapp_subject_subject_name_6082f2b1_uniq` (`subject_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_subject`
--

LOCK TABLES `searchapp_subject` WRITE;
/*!40000 ALTER TABLE `searchapp_subject` DISABLE KEYS */;
INSERT INTO `searchapp_subject` VALUES (1,'Science');
/*!40000 ALTER TABLE `searchapp_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `searchapp_subjectsplit`
--

DROP TABLE IF EXISTS `searchapp_subjectsplit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `searchapp_subjectsplit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `question_weightage` int(11) DEFAULT NULL,
  `question_type` int(11) DEFAULT NULL,
  `total_questions` int(11) NOT NULL,
  `questions_to_attempt` int(11) NOT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `searchapp_subjectspl_subject_id_9196c133_fk_searchapp` (`subject_id`),
  CONSTRAINT `searchapp_subjectspl_subject_id_9196c133_fk_searchapp` FOREIGN KEY (`subject_id`) REFERENCES `searchapp_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `searchapp_subjectsplit`
--

LOCK TABLES `searchapp_subjectsplit` WRITE;
/*!40000 ALTER TABLE `searchapp_subjectsplit` DISABLE KEYS */;
/*!40000 ALTER TABLE `searchapp_subjectsplit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-12  9:55:37
