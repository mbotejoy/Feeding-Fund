/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: feedingfund_db
-- ------------------------------------------------------
-- Server version	11.8.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add role',7,'add_role'),
(26,'Can change role',7,'change_role'),
(27,'Can delete role',7,'delete_role'),
(28,'Can view role',7,'view_role'),
(29,'Can add school',8,'add_school'),
(30,'Can change school',8,'change_school'),
(31,'Can delete school',8,'delete_school'),
(32,'Can view school',8,'view_school'),
(33,'Can add event',9,'add_event'),
(34,'Can change event',9,'change_event'),
(35,'Can delete event',9,'delete_event'),
(36,'Can view event',9,'view_event'),
(37,'Can add student',10,'add_student'),
(38,'Can change student',10,'change_student'),
(39,'Can delete student',10,'delete_student'),
(40,'Can view student',10,'view_student'),
(41,'Can add attendance',11,'add_attendance'),
(42,'Can change attendance',11,'change_attendance'),
(43,'Can delete attendance',11,'delete_attendance'),
(44,'Can view attendance',11,'view_attendance'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add feeding report',13,'add_feedingreport'),
(50,'Can change feeding report',13,'change_feedingreport'),
(51,'Can delete feeding report',13,'delete_feedingreport'),
(52,'Can view feeding report',13,'view_feedingreport'),
(53,'Can add feedback',14,'add_feedback'),
(54,'Can change feedback',14,'change_feedback'),
(55,'Can delete feedback',14,'delete_feedback'),
(56,'Can view feedback',14,'view_feedback'),
(57,'Can add event participation',15,'add_eventparticipation'),
(58,'Can change event participation',15,'change_eventparticipation'),
(59,'Can delete event participation',15,'delete_eventparticipation'),
(60,'Can view event participation',15,'view_eventparticipation'),
(61,'Can add donation',16,'add_donation'),
(62,'Can change donation',16,'change_donation'),
(63,'Can delete donation',16,'delete_donation'),
(64,'Can view donation',16,'view_donation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_user` VALUES
(1,'pbkdf2_sha256$870000$ENenFG31Fc93dzMdi9arpl$bXBNch5j9EYc2Sz57cLeTgDLKWleboQc34Nfq07tZLI=','2025-06-30 17:32:08.723343',1,'nyathirajoy@gmail.com','','','nyathirajoy@gmail.com',1,1,'2025-06-30 17:31:12.227819');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_attendance`
--

DROP TABLE IF EXISTS `core_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_attendance` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `attendance` varchar(255) NOT NULL,
  `attendance_date` date NOT NULL,
  `student_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_attendance_student_id_681381f8_fk_core_student_id` (`student_id`),
  CONSTRAINT `core_attendance_student_id_681381f8_fk_core_student_id` FOREIGN KEY (`student_id`) REFERENCES `core_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_attendance`
--

LOCK TABLES `core_attendance` WRITE;
/*!40000 ALTER TABLE `core_attendance` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_attendance` VALUES
(2,'1','2025-07-02',1);
/*!40000 ALTER TABLE `core_attendance` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_donation`
--

DROP TABLE IF EXISTS `core_donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_donation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `date` datetime(6) NOT NULL,
  `school_id` bigint(20) NOT NULL,
  `donor_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_donation_school_id_f94aced4_fk_core_school_id` (`school_id`),
  KEY `core_donation_donor_id_3af5d2f0_fk_core_user_id` (`donor_id`),
  CONSTRAINT `core_donation_donor_id_3af5d2f0_fk_core_user_id` FOREIGN KEY (`donor_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_donation_school_id_f94aced4_fk_core_school_id` FOREIGN KEY (`school_id`) REFERENCES `core_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_donation`
--

LOCK TABLES `core_donation` WRITE;
/*!40000 ALTER TABLE `core_donation` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `core_donation` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_event`
--

DROP TABLE IF EXISTS `core_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `event_date` date NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `school_id` bigint(20) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_event_created_by_id_55633c2b_fk_core_user_id` (`created_by_id`),
  KEY `core_event_school_id_a0d52eb6_fk_core_school_id` (`school_id`),
  CONSTRAINT `core_event_created_by_id_55633c2b_fk_core_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_event_school_id_a0d52eb6_fk_core_school_id` FOREIGN KEY (`school_id`) REFERENCES `core_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_event`
--

LOCK TABLES `core_event` WRITE;
/*!40000 ALTER TABLE `core_event` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_event` VALUES
(1,'Charity Event','Give back to the community','2025-06-30','2025-06-30 18:53:31.616759',1,1);
/*!40000 ALTER TABLE `core_event` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_eventparticipation`
--

DROP TABLE IF EXISTS `core_eventparticipation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_eventparticipation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `event_id` bigint(20) NOT NULL,
  `donor_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_eventparticipation_event_id_1db8d944_fk_core_event_id` (`event_id`),
  KEY `core_eventparticipation_donor_id_95bcd03f_fk_core_user_id` (`donor_id`),
  CONSTRAINT `core_eventparticipation_donor_id_95bcd03f_fk_core_user_id` FOREIGN KEY (`donor_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_eventparticipation_event_id_1db8d944_fk_core_event_id` FOREIGN KEY (`event_id`) REFERENCES `core_event` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_eventparticipation`
--

LOCK TABLES `core_eventparticipation` WRITE;
/*!40000 ALTER TABLE `core_eventparticipation` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_eventparticipation` VALUES
(1,1,3),
(2,1,6);
/*!40000 ALTER TABLE `core_eventparticipation` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_feedback`
--

DROP TABLE IF EXISTS `core_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_feedback` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_feedback_user_id_630c6a53_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_feedback_user_id_630c6a53_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_feedback`
--

LOCK TABLES `core_feedback` WRITE;
/*!40000 ALTER TABLE `core_feedback` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_feedback` VALUES
(1,'I enjoyed the event','2025-07-02 22:07:01.029686',2);
/*!40000 ALTER TABLE `core_feedback` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_feedingreport`
--

DROP TABLE IF EXISTS `core_feedingreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_feedingreport` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `report_date` date NOT NULL,
  `meals_received` int(11) NOT NULL,
  `meals_served` int(11) NOT NULL,
  `comments` longtext NOT NULL,
  `school` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_feedingreport`
--

LOCK TABLES `core_feedingreport` WRITE;
/*!40000 ALTER TABLE `core_feedingreport` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_feedingreport` VALUES
(1,'2025-06-30',2,2,'Served tea break and lunch','Valley Bridge','Grace'),
(2,'2025-06-30',2,2,'no comments','Valley Bridge','Grace'),
(3,'2025-06-30',1,2,'no comments','Valley Bridge','Grace');
/*!40000 ALTER TABLE `core_feedingreport` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_role`
--

DROP TABLE IF EXISTS `core_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_role`
--

LOCK TABLES `core_role` WRITE;
/*!40000 ALTER TABLE `core_role` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_role` VALUES
(14,'school admin'),
(15,'community agent'),
(16,'donor'),
(17,'parent');
/*!40000 ALTER TABLE `core_role` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_school`
--

DROP TABLE IF EXISTS `core_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_school` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `school_name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_school`
--

LOCK TABLES `core_school` WRITE;
/*!40000 ALTER TABLE `core_school` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_school` VALUES
(1,'Valley Bridge School','Kariobangi','valleybridgeschool@gmail.com','07123456789','2025-06-30 17:16:02.882670');
/*!40000 ALTER TABLE `core_school` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_student`
--

DROP TABLE IF EXISTS `core_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `grade` int(11) NOT NULL,
  `school_id` bigint(20) NOT NULL,
  `parent_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_student_parent_id_60157d65_fk_core_user_id` (`parent_id`),
  KEY `core_student_school_id_9d30b4f7_fk_core_school_id` (`school_id`),
  CONSTRAINT `core_student_parent_id_60157d65_fk_core_user_id` FOREIGN KEY (`parent_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_student_school_id_9d30b4f7_fk_core_school_id` FOREIGN KEY (`school_id`) REFERENCES `core_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_student`
--

LOCK TABLES `core_student` WRITE;
/*!40000 ALTER TABLE `core_student` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_student` VALUES
(1,'Faith Waliaula',4,1,2);
/*!40000 ALTER TABLE `core_student` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(128) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `role_id` bigint(20) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_verified` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `core_user_role_id_8de62872_fk_core_role_id` (`role_id`),
  CONSTRAINT `core_user_role_id_8de62872_fk_core_role_id` FOREIGN KEY (`role_id`) REFERENCES `core_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `core_user` VALUES
(1,'Joy Mbote','ga@gmail.com','pbkdf2_sha256$870000$7whZ1EppO26j1LkBcrGJS5$mVnLrfGppZ7ysb8PgZ2mBpa87nX0LLTS5gBuwSdvTVQ=','2025-06-26 12:56:36.787941',15,1,0,0,NULL,0),
(2,'Paul Waliaula','pwaliaula@gmail.com','pbkdf2_sha256$870000$dpBpE1yYs1ACJd8SZJOQbb$BaZse+PgrJV22Yye87rgDAlcP2X55/j5x4l/C3LDjOY=','2025-06-30 19:25:59.234456',17,1,0,0,NULL,0),
(3,'Fred Kimemia','kimemiafred@gmail.com','pbkdf2_sha256$870000$TYb5J02uA1w7bn7WoUtWAB$MFvlCEnNjUagHTg/P3m0egMmwl87h72VphhZEwFxJt4=','2025-06-30 20:26:17.724241',16,1,0,0,NULL,0),
(4,'Joyce','joyce@gmail.com','pbkdf2_sha256$870000$94VN2kQhn28qym8g11gZPt$Bc2XbmlmtAySgsdMV/JQ19m767gRCpa3KLtL2mSr3FU=','2025-07-02 18:29:13.946039',15,1,0,0,NULL,0),
(5,'Joyce Atieno','jatieno@gmail.com','pbkdf2_sha256$870000$TalCOcqoJG03AuG0QgU91T$2GRBTPciYUUxRINZwL6ebN12VI4rBQWPxtTiTE70A5w=','2025-07-02 18:31:20.174527',15,1,0,0,'2025-07-06 09:00:29.763664',0),
(6,'Juliet Ndambuki','ndambukij@gmail.com','pbkdf2_sha256$870000$sT0wPx3FXUQlcJRvvcg9zL$jcifpirbxsM5PLdO/TygMIwEuLZF942anqZ51PZPsA8=','2025-07-03 09:08:49.716472',16,1,0,0,'2025-07-03 09:51:00.990570',0),
(7,'Juliet Ndambuki','jn@gmail.com','pbkdf2_sha256$870000$ngSSjXcnZ6WZ5e51bXFEIK$nTKtf3DD9lAnW8Kjiu0HiE4uQC2yVwkmSW/djwqk+1c=','2025-07-03 10:52:26.266404',14,1,0,0,'2025-07-03 10:52:48.728982',0),
(8,'Joy Mbote','jm@gmail.com','pbkdf2_sha256$870000$kHZQjiEcnuorIESmMjnY2s$0UA8UENL4V6VW6ZGM+zanpK48YLrFWI9hbpegmPeO5I=','2025-07-06 07:43:54.585560',14,1,0,0,'2025-07-06 07:44:16.923919',0),
(10,'','joy.mbote@strathmore.edu','pbkdf2_sha256$870000$s6Fggq81CRLhGccSDT0t0G$bKflGgbDxdFYcBASEbisD8thhAaBywTG0IO3r+dHsnI=','2025-07-06 10:02:45.718762',NULL,1,1,1,'2025-07-06 10:03:55.302573',0);
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(11,'core','attendance'),
(16,'core','donation'),
(9,'core','event'),
(15,'core','eventparticipation'),
(14,'core','feedback'),
(13,'core','feedingreport'),
(7,'core','role'),
(8,'core','school'),
(10,'core','student'),
(12,'core','user'),
(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-06-21 21:18:42.204289'),
(2,'auth','0001_initial','2025-06-21 21:18:42.598686'),
(3,'admin','0001_initial','2025-06-21 21:18:42.678629'),
(4,'admin','0002_logentry_remove_auto_add','2025-06-21 21:18:42.688787'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-06-21 21:18:42.695926'),
(6,'contenttypes','0002_remove_content_type_name','2025-06-21 21:18:42.765655'),
(7,'auth','0002_alter_permission_name_max_length','2025-06-21 21:18:42.789405'),
(8,'auth','0003_alter_user_email_max_length','2025-06-21 21:18:42.821072'),
(9,'auth','0004_alter_user_username_opts','2025-06-21 21:18:42.831302'),
(10,'auth','0005_alter_user_last_login_null','2025-06-21 21:18:42.870073'),
(11,'auth','0006_require_contenttypes_0002','2025-06-21 21:18:42.872634'),
(12,'auth','0007_alter_validators_add_error_messages','2025-06-21 21:18:42.884966'),
(13,'auth','0008_alter_user_username_max_length','2025-06-21 21:18:42.913335'),
(14,'auth','0009_alter_user_last_name_max_length','2025-06-21 21:18:42.940847'),
(15,'auth','0010_alter_group_name_max_length','2025-06-21 21:18:42.964109'),
(16,'auth','0011_update_proxy_permissions','2025-06-21 21:18:42.981674'),
(17,'auth','0012_alter_user_first_name_max_length','2025-06-21 21:18:43.006341'),
(18,'core','0001_initial','2025-06-21 21:18:43.558113'),
(19,'sessions','0001_initial','2025-06-21 21:18:43.588413'),
(20,'core','0002_rename_role_role_name','2025-06-26 11:24:39.444596'),
(21,'core','0003_alter_role_name','2025-06-26 11:37:06.835613'),
(22,'core','0004_alter_feedingreport_school_alter_feedingreport_user','2025-06-30 16:49:37.949091'),
(23,'core','0005_user_groups_user_is_active_user_is_staff_and_more','2025-07-02 19:30:14.374972'),
(24,'core','0006_alter_attendance_attendance','2025-07-02 21:12:29.124796'),
(25,'core','0007_alter_role_name_alter_user_role','2025-07-06 09:26:35.453814'),
(26,'core','0008_user_is_verified','2025-07-06 09:47:21.474899');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_session` VALUES
('6qm8dawhb1w4powu7jhdwpy1mz5g6gmi','e30:1uX2sY:dfTpM6ytnEmMGYIs-7iG7dzOdMagHyceAKhR_0ok7i0','2025-07-16 19:12:22.608702'),
('u3mi8cbh9gneiekgtic3jexa3iopnqdh','.eJxVjDsOwjAQBe_iGlmO_6akzxmsza6NA8iW4qRC3J1ESgHtzLz3ZhG2tcStpyXOxK5sEOzyCyfAZ6qHoQfUe-PY6rrMEz8SftrOx0bpdTvbv4MCvexrEQbvSFsK3gulCFAEa8DlrLQCq7O0bgdOo7QyeZNzshmlCkhCJzTs8wXiWDeV:1uYMDz:N5x5Mv8yHW6hSKo8adfJtJ9Z5JfgURlxI0db619DtYI','2025-07-20 10:03:55.302573'),
('vy540yll3yyyos9w5r6gi7gg8nwc46ye','.eJxVjMsOwiAQRf-FtSHIG5fu-w1kmAGpGkhKuzL-uzbpQrf3nHNfLMK21riNvMSZ2IV5dvrdEuAjtx3QHdqtc-xtXebEd4UfdPCpU35eD_fvoMKo31rb4EWwqgRhAqFDE84la0cWEpKTIllAb0sRgFIbwqKKIJTWq4xoNHt_AOZ2OHo:1uYK2q:HeGOlXkrkjlIQed_tNPpm3ZnTAYHvHCIcUUFkcNoG24','2025-07-20 07:44:16.732064'),
('wrnwur8fssvbgeavqxpqgxtj36k3toii','e30:1uX2rW:_y9DNZ6emD0zFSBVYQeHr8dtW_2CUo-x2qIVqnicc00','2025-07-16 19:11:18.393234');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-07-06 13:16:18
