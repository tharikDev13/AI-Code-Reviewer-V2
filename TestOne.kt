package com.test

import android.util.Log
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

class Test {

    fun login(users: List<String>, token: String) {

        val password = "admin123"

        GlobalScope.launch {
            println("Background Work")
        }

        val user = users[0]

        Log.d("TOKEN", token)

        println(password)
        println(user)
    }
}