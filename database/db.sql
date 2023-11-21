-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.28-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table test.mark: ~5 rows (approximately)
DELETE FROM `mark`;
INSERT INTO `mark` (`Student_ID`, `Toán`, `Lý`, `Hóa`, `Sinh`, `Sử`, `Văn`, `Anh`, `Tin`) VALUES
	(0, 10, 10, 10, 10, 10, 10, 10, 10),
	(1, 10, 10, 10, 10, 10, 10, 10, 10),
	(2, 10, 10, 10, 10, 10, 10, 10, 10),
	(3, 10, 10, 10, 10, 10, 10, 10, 10),
	(4, 9, 9, 9, 9, 9, 9, 9, 9);

-- Dumping data for table test.student: ~5 rows (approximately)
DELETE FROM `student`;
INSERT INTO `student` (`Student_ID`, `Students`, `Class`, `Sex`, `Birth`, `Hanhkiem`) VALUES
	(0, 'Nguyen Huu Khanh', '11A1', 'Nam', '2007-09-09', 'Tot'),
	(1, 'Nguyen Ba Dung', '11A1', 'Nam', '2023-11-04', 'Tot'),
	(2, 'Tran Sy Hung', '11A1', 'Nam', '2007-10-10', 'Tot'),
	(3, 'Cung Dinh Tien ', '11A1', 'Nam', '1999-01-01', 'Tot'),
	(4, 'Ho Sy Phu', '11A1', 'Nu', '1999-01-01', 'Tot');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
