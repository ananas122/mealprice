-- MySQL dump 10.13  Distrib 8.1.0, for macos13.3 (arm64)
--
-- Host: localhost    Database: mp_db
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `start_datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Votre type d\'événement ici - Recette non trouvée','2023-10-23 00:00:00'),(2,'Votre type d\'événement ici - Recette non trouvée','2023-10-23 00:00:00'),(3,'Votre type d\'événement ici - Recette non trouvée','2023-10-25 00:00:00'),(4,'test','2023-10-21 15:00:00'),(5,'Breakfast - Hotcakes','2023-10-25 09:00:00'),(6,'Breakfast - Hotcakes','2023-10-25 09:00:00'),(7,'Dîner - Gyros','2023-10-31 10:11:00'),(8,'Birthday - PB and J Overnight Oatmeal','2023-11-01 10:11:00'),(9,'Dîner - Dump Cake','2023-11-29 00:00:00'),(10,'Birthday - PB and J Overnight Oatmeal','2023-10-31 10:11:00'),(11,'Dîner - Asparagus Quiche','2024-01-24 11:59:00'),(12,'Dîner - Asparagus Quiche','2024-01-24 11:59:00'),(13,'Dîner - Coffee & Banana Pie (Pastel de Cafe y Bananos)','2024-02-02 11:59:00'),(14,'Dîner - Asparagus Quiche','2024-01-24 11:59:00'),(15,'Dîner - Coffee & Banana Pie (Pastel de Cafe y Bananos)','2024-02-02 11:59:00'),(16,'Dîner - Frittata','2023-10-25 09:11:00'),(17,'Dîner - Recette non trouvée','2023-10-27 10:00:00'),(18,'Dîner - Pancakes','2023-11-01 11:00:00'),(19,'Dîner - Recette non trouvée','2023-10-27 10:00:00'),(20,'Dîner - Pancakes','2023-11-01 11:00:00'),(21,'Dîner - Asparagus Quiche','2023-11-01 21:00:00'),(22,'Birthday - Cake Balls','2024-02-16 21:00:00'),(23,'Dîner - Gyros','2023-10-19 09:59:00'),(24,'Dîner - Asparagus Quiche','2023-11-01 02:59:00'),(25,'Dîner - Asparagus Quiche','2023-10-26 10:22:00'),(26,'Dîner - Asparagus Quiche','2023-10-26 10:22:00'),(27,'Birthday - A Bag Pudding With Currants','2023-10-27 10:22:00'),(28,'Dîner - Gyros','2023-10-31 10:59:00'),(29,'Dîner - Salsa','2023-11-02 10:59:00'),(30,'Dîner - Hotcakes','2023-11-03 06:00:00'),(31,'Dîner - Asparagus Quiche','2023-11-09 22:00:00'),(32,'Dîner - A Bag Pudding With Currants','2024-01-17 10:00:00'),(33,'Dîner - A Bag Pudding With Currants','2024-01-17 10:00:00'),(34,'Dîner - A Bag Pudding With Currants','2024-01-17 10:00:00'),(35,'Dîner - A Bag Pudding With Currants','2024-01-17 10:00:00'),(36,'Dîner - Asparagus Quiche','2023-11-09 22:00:00'),(37,'Dîner - Bagels','2024-01-17 10:22:00');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Quantité_en_stock` int NOT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `Catégorie` varchar(255) DEFAULT NULL,
  `Coût_unitaire` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'john_doe','a7af71ad2b0ce07c36781ab7c8a6d36bd703824c22647f85d6de62063b219bc6',NULL,NULL,NULL),(2,'sam_no','f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae','sss@yahoo.fr','sam','no');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-01 10:45:51
