-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2023 at 08:27 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `informatica1`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `id` int(3) NOT NULL,
  `code` varchar(4) NOT NULL,
  `name` varchar(100) NOT NULL,
  `number` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`id`, `code`, `name`, `number`) VALUES
(1, '1234', 'Hospital San Vicente', 4441333),
(2, '5678', 'Hospital Pablo Tobón Uribe', 4459000);

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `id` int(3) NOT NULL,
  `lote` int(4) NOT NULL,
  `name` varchar(50) NOT NULL,
  `distributor` varchar(50) NOT NULL,
  `stock` int(3) NOT NULL,
  `date` date NOT NULL,
  `price` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`id`, `lote`, `name`, `distributor`, `stock`, `date`, `price`) VALUES
(1, 111, 'Sertralina', 'Drogas Cafam', 20, '2023-05-24', 5000),
(2, 222, 'Fluoxetina', 'Cruz Verde', 10, '2023-05-02', 8000),
(3, 333, 'Clonazepam', 'Genfar', 100, '2023-03-11', 3000),
(4, 444, 'Rivotril', 'Farmatodo', 50, '2022-12-24', 5000),
(5, 555, 'Loratadina', 'MK', 45, '2023-05-31', 800),
(6, 666, 'Hidroxicina', 'La Santé', 200, '2023-04-01', 500),
(7, 999, 'Carbamol', 'Farmatodo', 10, '2022-09-12', 800);

-- --------------------------------------------------------

--
-- Table structure for table `provider`
--

CREATE TABLE `provider` (
  `id` int(3) NOT NULL,
  `code` int(4) NOT NULL,
  `name` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `identify` int(10) NOT NULL,
  `company` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `provider`
--

INSERT INTO `provider` (`id`, `code`, `name`, `lastname`, `identify`, `company`) VALUES
(1, 101, 'Jorge Andrés', 'Camacho', 1008902138, 'Laboratorios Ubiopharma'),
(2, 202, 'María Camila', 'Arias Restrepo', 1122334455, 'Mediservis'),
(3, 303, 'Valentina', 'Marquez Lora', 2147483647, 'Productos Roché ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `provider`
--
ALTER TABLE `provider`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `location`
--
ALTER TABLE `location`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `provider`
--
ALTER TABLE `provider`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
