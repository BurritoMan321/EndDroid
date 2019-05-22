package com.example.enddroids;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private Button start;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        start = (Button) findViewById(R.id.button1);
        start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               start();
            }
        });
    }
    public void start(){
        Intent intent = new Intent(this, enddroids2.class);
        startActivity(intent);
    }
}
