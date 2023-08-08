-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema blogs_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema blogs_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blogs_schema` DEFAULT CHARACTER SET utf8 ;
USE `blogs_schema` ;

-- -----------------------------------------------------
-- Table `blogs_schema`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`Blogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Blogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`admins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Blog_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_Blogs_has_Users_Users1_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Blogs_has_Users_Blogs1_idx` (`Blog_id` ASC) VISIBLE,
  CONSTRAINT `fk_Blogs_has_Users_Blogs1`
    FOREIGN KEY (`Blog_id`)
    REFERENCES `blogs_schema`.`Blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Blogs_has_Users_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blogs_schema`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`Posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `content` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `admin_id` INT NOT NULL,
  `Blog_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Posts_admins1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_Posts_Blogs1_idx` (`Blog_id` ASC) VISIBLE,
  CONSTRAINT `fk_Posts_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs_schema`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Posts_Blogs1`
    FOREIGN KEY (`Blog_id`)
    REFERENCES `blogs_schema`.`Blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `content` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `Post_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Comments_Posts1_idx` (`Post_id` ASC) VISIBLE,
  INDEX `fk_Comments_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Comments_Posts1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `blogs_schema`.`Posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Comments_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `blogs_schema`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`Files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Files` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `Post_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Files_Posts1_idx` (`Post_id` ASC) VISIBLE,
  INDEX `fk_Files_admins1_idx` (`admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_Files_Posts1`
    FOREIGN KEY (`Post_id`)
    REFERENCES `blogs_schema`.`Posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Files_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs_schema`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`Page_views`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`Page_views` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Blog_id` INT NOT NULL,
  `User_id` INT NOT NULL,
  `ip_address` VARCHAR(16) NULL,
  `view_length` DECIMAL NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_Blogs_has_Users_Users2_idx` (`User_id` ASC) VISIBLE,
  INDEX `fk_Blogs_has_Users_Blogs2_idx` (`Blog_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Blogs_has_Users_Blogs2`
    FOREIGN KEY (`Blog_id`)
    REFERENCES `blogs_schema`.`Blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Blogs_has_Users_Users2`
    FOREIGN KEY (`User_id`)
    REFERENCES `blogs_schema`.`Users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
