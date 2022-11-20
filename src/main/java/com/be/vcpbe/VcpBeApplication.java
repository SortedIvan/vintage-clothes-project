package com.be.vcpbe;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class })
public class VcpBeApplication {

	public static void main(String[] args) {
		SpringApplication.run(VcpBeApplication.class, args);
	}

}
