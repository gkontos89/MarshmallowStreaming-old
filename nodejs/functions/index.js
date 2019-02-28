const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();
const db = admin.database();

/**
 * Questionnaire Processing
 * 
 * This cloud function scans for submitted questionnaires then processes the recommended 
 * packages based on the data
 * 
 * listens - /unprocessedQuestionnaires/{uid}: data
 * post - /questionnaires/{uid}: data
 * post - /recommendations/{uid}: data
 * post - /clients/{clientUid}/questionnaires/{uid}: true
 */
exports.questionnaireScanner = functions.database.ref('/unprocessedQuestionnaires/{uid}')
    .onCreate((snapshot, context) => {
        var uid = context.params.uid;
        const questionnaireData = snapshot.val();
        console.log("UID=", uid);
        
        // Compute recommendation
        if (questionnaireData === "psvue") {
            console.log("psvue");
        } else {
            console.log("youtube")
        }


        // Store questionnaire in /questionnaires
        var questionnaireRef = db.ref("questionnaires")
        questionnaireRef.child(uid).set(questionnaireData);

        
        // Store recommendation in /recommendations
        var recommendation = db.ref("recommendations")
        return recommendation.child(uid).set("heyo")

        // Delete unprocessedQuestionnaire entry
                
});

/**
 * Marshmallow Service Processing
 * 
 * This cloud function processes Marshmallow service appointments which capture all work done including
 * package updates, equipment installed, ect.
 * 
 * listens - /unprocessedMarshmallowServiceSubmittals/{uid}: data
 * post - /clients/{clientUid}/marshmallowService/{uid}: true
 * post - /marshmallowServices/{uid}: data
 * post - /businessMetrics/*applicable fields
 */
exports.marshmallowServiceProcessing = functions.database.ref('/unprocessedMarshmallowServiceSubmittals')
    .onCreate((snapshot, context) => {
        
})

/**
 * Original Service Capture Processing
 * 
 * This cloud function processes the capture of a new clients original services before being serviced by
 * Marshmallow.  This will include data from their current bill, equipment rentals and any other aspects
 * of their service
 * 
 * listens - /unprocessedOriginalServiceCaptures/{uid}: data
 * post - /originalServiceCaptures/{uid}: data
 * post - /clients/{clientUid}/originalServiceCapture/{uid}: true
 * post = /businessMetrics/*applicable fields
 */
