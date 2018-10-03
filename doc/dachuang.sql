

/*用户表*/
CREATE TABLE IF NOT EXISTS `t_user`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `username` VARCHAR(64) NOT NULL,
   `password` VARCHAR(64) NOT NULL,
   `create_time` DATE,
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


/*用户角色表*/
CREATE TABLE IF NOT EXISTS `t_role`(
  `id` INT UNSIGNED AUTO_INCREMENT,
  `roleName` VARCHAR (32) NOT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*权限表数据*/
CREATE TABLE IF NOT EXISTS `t_permission`(
  `id` INT UNSIGNED AUTO_INCREMENT,
  `permissionName` VARCHAR (32) NOT NULL,
  `permissionLabel` VARCHAR (32) NOT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*用户角色关联表*/
CREATE TABLE IF NOT EXISTS `t_user_role`(
  `userId` INT UNSIGNED NOT NULL,
  `roleId` INT UNSIGNED NOT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*角色权限关联表*/
CREATE TABLE IF NOT EXISTS `t_role_permission`(
  `roleId` INT UNSIGNED NOT NULL,
  `permissionId` INT UNSIGNED NOT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `t_role_permission`(
  `roleId` INT UNSIGNED NOT NULL,
  `permissionId` INT UNSIGNED NOT NULL,
)ENGINE=InnoDB DEFAULT CHARSET=utf8;






