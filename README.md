# Knowledge Base (KB) of symptoms.
The Knowledge Base (KB) system is a HTTP-based REST API that provides access to the pre-trained topic model. KB implmentation is part of CO-ADAPT project. We hope the KB can be useful, adapted for implentation of conversational agent or electronic medical records analysis system to help therapists with symptom recommendations. 

![alt text](https://coadapt-project.eu/wp-content/uploads/2019/02/cropped-5_coadapt_logo_blu_small-1.jpg)

Installation instruction:

npm install

npm run dev-start


Sample Input to the API:


{
    "code": "questionCode",
    "content": "I've always been a bad sleeper. Used to wake up lots of times at night and would wake up in the morning feeling tired and not rested. It improved after my early 20's and after I left University. Curiosly, ever since I joined the Police Force and started doing shifts, even though I hate them and feel how prejudicial they are, I've been sleeping better when im off shift.",
    "participantID": "123456123456123456123456",
    "responseTime": 5897,
    "gender": "Male",
    "workHours": 42,
    "control": "A fair amount",
    "description_Problems": "",
    "satisfaction_General": "Entirely dissatisfied",
    "satisfaction_Sleep": "Dissatisfied",
    "satisfaction_SleepEnvironment": "Very suitable",
    "satisfaction_Diet": "Very suitable",
    "satisfaction_Exercise": "Very suitable"
}

