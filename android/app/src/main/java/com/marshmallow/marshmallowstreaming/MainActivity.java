package com.marshmallow.marshmallowstreaming;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity {
    FirebaseDatabase db;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        db = FirebaseDatabase.getInstance();
        Button psvue = findViewById(R.id.PSVue_button);
        Button youtube = findViewById(R.id.YouTubeTV_button);
        TextView response = findViewById(R.id.response);

        psvue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DatabaseReference ref = db.getReference("unprocessedQuestionnaires");
                String uid = ref.push().getKey();
                if (uid != null) {
                    ref.child(uid).setValue("psvue");
                }
            }
        });

        youtube.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DatabaseReference ref = db.getReference("unprocessedQuestionnaires");
                String uid = ref.push().getKey();
                if (uid != null) {
                    ref.child(uid).setValue("youtube");
                }
            }
        });
    }
}
