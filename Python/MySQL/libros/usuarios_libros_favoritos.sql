-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_libros` ;

-- -----------------------------------------------------
-- Schema esquema_libros
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_libros` ;
USE `esquema_libros` ;

-- -----------------------------------------------------
-- Table `esquema_libros`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tittle` VARCHAR(45) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros`.`favorites` (
  `user_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  INDEX `fk_favorites_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_favorites_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorites_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_libros`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `esquema_libros`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
