package com.be.vcpbe.api;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;

@RestController
public class TestController {

    @CrossOrigin(origins = "http://localhost:8080")
    @GetMapping("/greet/{user}")
    public String greetUser(@PathVariable(value="user") String user){
        return String.format("Hello, %s", user);
    }
}
