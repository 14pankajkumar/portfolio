-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 31, 2020 at 06:56 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myportfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `about`
--

CREATE TABLE `about` (
  `sno` int(11) NOT NULL,
  `about_head` text NOT NULL,
  `heading` text NOT NULL,
  `about_details` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `about`
--

INSERT INTO `about` (`sno`, `about_head`, `heading`, `about_details`) VALUES
(1, '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `apps`
--

CREATE TABLE `apps` (
  `sno` int(11) NOT NULL,
  `app_img` varchar(20) NOT NULL,
  `app_url` varchar(100) NOT NULL,
  `slug` varchar(20) NOT NULL,
  `app_title` varchar(100) NOT NULL,
  `app_content` text NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `card`
--

CREATE TABLE `card` (
  `sno` int(11) NOT NULL,
  `card_img` varchar(20) NOT NULL,
  `card_url` varchar(100) NOT NULL,
  `slug` varchar(20) NOT NULL,
  `card_title` varchar(100) NOT NULL,
  `card_content` text NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `subject` text NOT NULL,
  `date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `subject`, `date`) VALUES
(1, 'Pankaj Kumar', 'pankajkumardas727@gm', 'I want to ask that what do you do??', 'Sun Dec 27 18:07:43 '),
(2, 'Pankaj Kumar', 'pankajkumardas727@gm', 'I want to ask that what do you do??', 'Sun Dec 27 19:24:45 '),
(3, '', '', '', 'Mon Dec 28 21:15:00 '),
(4, 'Pankaj Kumar', 'pankajkumardas727@gm', 'I want to ask that what do you do??', 'Thu Dec 31 21:40:53 '),
(5, 'Pankaj Kumar', 'pankajkumardas727@gm', 'I want to ask that what do you do??', 'Thu Dec 31 21:45:47 ');

-- --------------------------------------------------------

--
-- Table structure for table `credentials`
--

CREATE TABLE `credentials` (
  `sno` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `credentials`
--

INSERT INTO `credentials` (`sno`, `username`, `password`, `email`) VALUES
(1, 'username', '12345', 'example@email.com');

-- --------------------------------------------------------

--
-- Table structure for table `education`
--

CREATE TABLE `education` (
  `sno` int(11) NOT NULL,
  `course` varchar(100) NOT NULL,
  `year` varchar(20) NOT NULL,
  `institute` varchar(100) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `facthead`
--

CREATE TABLE `facthead` (
  `sno` int(11) NOT NULL,
  `fact_head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `facthead`
--

INSERT INTO `facthead` (`sno`, `fact_head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `facts`
--

CREATE TABLE `facts` (
  `sno` int(11) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `fact` varchar(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `portfolio`
--

CREATE TABLE `portfolio` (
  `sno` int(11) NOT NULL,
  `portfolio_head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `portfolio`
--

INSERT INTO `portfolio` (`sno`, `portfolio_head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `proex`
--

CREATE TABLE `proex` (
  `sno` int(11) NOT NULL,
  `course` varchar(100) NOT NULL,
  `year` varchar(20) NOT NULL,
  `company` varchar(100) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `sno` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_mail` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `location_url` varchar(500) NOT NULL,
  `location_map` varchar(500) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `call_url` varchar(20) NOT NULL,
  `website` varchar(50) NOT NULL,
  `pro_img` varchar(20) NOT NULL,
  `bg_img` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`sno`, `name`, `dob`, `email`, `send_mail`, `location`, `location_url`, `location_map`, `phone_num`, `call_url`, `website`, `pro_img`, `bg_img`) VALUES
(1, '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `resume`
--

CREATE TABLE `resume` (
  `sno` int(11) NOT NULL,
  `resume_head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resume`
--

INSERT INTO `resume` (`sno`, `resume_head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `resumesummary`
--

CREATE TABLE `resumesummary` (
  `sno` int(11) NOT NULL,
  `summary` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `resumesummary`
--

INSERT INTO `resumesummary` (`sno`, `summary`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `servicehead`
--

CREATE TABLE `servicehead` (
  `sno` int(11) NOT NULL,
  `head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `servicehead`
--

INSERT INTO `servicehead` (`sno`, `head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `sno` int(11) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `link` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `skillhead`
--

CREATE TABLE `skillhead` (
  `sno` int(11) NOT NULL,
  `head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skillhead`
--

INSERT INTO `skillhead` (`sno`, `head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE `skills` (
  `sno` int(11) NOT NULL,
  `skills_data` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `social`
--

CREATE TABLE `social` (
  `sno` int(11) NOT NULL,
  `github` varchar(50) NOT NULL,
  `youtube` varchar(50) NOT NULL,
  `twitter` varchar(50) NOT NULL,
  `instagram` varchar(50) NOT NULL,
  `linkedin` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `social`
--

INSERT INTO `social` (`sno`, `github`, `youtube`, `twitter`, `instagram`, `linkedin`) VALUES
(1, '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `testimonials`
--

CREATE TABLE `testimonials` (
  `sno` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `occupation` varchar(50) NOT NULL,
  `comment` text NOT NULL,
  `img` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `thead`
--

CREATE TABLE `thead` (
  `sno` int(11) NOT NULL,
  `head` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `thead`
--

INSERT INTO `thead` (`sno`, `head`) VALUES
(1, '');

-- --------------------------------------------------------

--
-- Table structure for table `web`
--

CREATE TABLE `web` (
  `sno` int(11) NOT NULL,
  `web_img` varchar(20) NOT NULL,
  `web_url` varchar(100) NOT NULL,
  `slug` varchar(20) NOT NULL,
  `web_title` varchar(100) NOT NULL,
  `web_content` text NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `about`
--
ALTER TABLE `about`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `apps`
--
ALTER TABLE `apps`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `card`
--
ALTER TABLE `card`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `education`
--
ALTER TABLE `education`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `facthead`
--
ALTER TABLE `facthead`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `facts`
--
ALTER TABLE `facts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `portfolio`
--
ALTER TABLE `portfolio`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `proex`
--
ALTER TABLE `proex`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `resume`
--
ALTER TABLE `resume`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `resumesummary`
--
ALTER TABLE `resumesummary`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `servicehead`
--
ALTER TABLE `servicehead`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `skillhead`
--
ALTER TABLE `skillhead`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `social`
--
ALTER TABLE `social`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `testimonials`
--
ALTER TABLE `testimonials`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `thead`
--
ALTER TABLE `thead`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `web`
--
ALTER TABLE `web`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `about`
--
ALTER TABLE `about`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `apps`
--
ALTER TABLE `apps`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `card`
--
ALTER TABLE `card`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `credentials`
--
ALTER TABLE `credentials`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `education`
--
ALTER TABLE `education`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `facthead`
--
ALTER TABLE `facthead`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `facts`
--
ALTER TABLE `facts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `portfolio`
--
ALTER TABLE `portfolio`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `proex`
--
ALTER TABLE `proex`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `resume`
--
ALTER TABLE `resume`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `resumesummary`
--
ALTER TABLE `resumesummary`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `servicehead`
--
ALTER TABLE `servicehead`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `skillhead`
--
ALTER TABLE `skillhead`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `skills`
--
ALTER TABLE `skills`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `social`
--
ALTER TABLE `social`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `testimonials`
--
ALTER TABLE `testimonials`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `thead`
--
ALTER TABLE `thead`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `web`
--
ALTER TABLE `web`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
