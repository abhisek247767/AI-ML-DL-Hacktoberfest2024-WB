// ------------Importing Data--------------
let name = "";
let age = "";
let gender = "";
let symptoms = [];
let rejected_symptoms = [];
let disease = [];
let recommended_symptoms = [];
let remedyData = {};

$(document).ready(function () {
    // Initialize tooltip
    $('.nav-tabs > li a[title]').tooltip();
    //Wizard
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        var $target = $(e.target);
        if ($target.hasClass('disabled')) {
            return false;
        }
      
        // handle with prgressbar 
        var step = $(e.target).data('step');
        var percent = (parseInt(step) / 4) * 100;
        $('.progress-bar').css({ width: percent + '%' });
        $('.progress-bar').text('Step ' + step + ' of 4');
      
    });

    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {
        var $target = $(e.target);
        $target.parent().addClass('active');
    });

    $('a[data-toggle="tab"]').on('hide.bs.tab', function (e) {
        var $target = $(e.target);
        $target.parent().removeClass('active');
    });

    $(".next-step").click(function (e) {
        var $active = $('.wizard .nav-tabs li a.active');
        $active.parent().next().children().removeClass('disabled');
        $active.parent().addClass('done');
        var step = $active.data('step');
        handleStepChange(step);
        nextTab($active);
    });

    handleStep1();
});

function nextTab(elem) {
    $(elem).parent().next().find('a[data-toggle="tab"]').click();
}

function fixString(str) {
    return str.replace(/_/g, ' ').split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

function getRele(array, numElements) {
    let rele = [];
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    for (let i = 0; i < numElements; i++) {
        rele.push(array[i]);
    }
    return rele;
}  

async function fetchNewSymptoms() {
    let res = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({symptoms: symptoms, age: age, gender: gender, rejected_symptoms: rejected_symptoms}),
    });
    let data = await res.json();
    disease = data.top_diseases;
    recommended_symptoms = data.top_symptoms;
}

function typeMessageWithDelay(message, delay) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(message);
      }, delay);
    });
  }

async function addMessageWithTypingEffect(message, containerId) {
    var chatboxContent = document.getElementById(containerId);
    var typingSpeed = 40; 

      for (let char of message) {
        chatboxContent.innerHTML += char;
        await typeMessageWithDelay("", typingSpeed);
      }
    chatboxContent.innerHTML += "<br>"; 
  }

async function addMessageForQuestion(index) {
    document.getElementById("questionBox-step3").innerHTML = `
        <p id="question-step3"></p>
    `;
    var questionContent = document.getElementById("question-step3");
    var typingSpeed = 40; 
    var symp = fixString(recommended_symptoms[index]);
    var message = `Did you experience symptoms like ${symp} ?`;
     for (let char of message) {
        questionContent.innerHTML += char;
        await typeMessageWithDelay("", typingSpeed);
      }

    questionContent.innerHTML += "<br>"; 
    document.getElementById("questionBox-step3").innerHTML += `
      <button class="btn btn-success btn-sm mr-2" id="btn-yes">YES</button>
      <button class="btn btn-danger btn-sm" id="btn-no">NO</button>
    `;

    document.getElementById("btn-no").addEventListener("click", function() {
        console.log("No");
        rejected_symptoms.push(recommended_symptoms[index]);
        askQuestion(index + 1);
    });

    document.getElementById("btn-yes").addEventListener("click", async function() {
        console.log("Yes");
        symptoms.push(recommended_symptoms[index]);
        console.log(symptoms);
        document.getElementById("questionBox-step3").innerHTML = `hmm... let me rethink based on ${fixString(recommended_symptoms[index])} symptom.`;
        await fetchNewSymptoms();
        askQuestion(0);
    });
  }

async function askQuestion(index) {
    if(symptoms.length > 6){
        document.getElementById("questionBox-step3").innerHTML = "";
        addMessageWithTypingEffect("Fine... I got enough information to diagnose your disease. 🎉", "questionBox-step3")
        .then(() => addMessageWithTypingEffect("", "questionBox-step3"))
        .then(() => addMessageWithTypingEffect(`For symptoms like ${symptoms.map(sym => fixString(sym)).join(', ')},
        you may have ${fixString(disease[0])}.`, "questionBox-step3"))
        .then(() => addMessageWithTypingEffect("", "questionBox-step3"))
        .then(() => addMessageWithTypingEffect("Click on 'Get Insights' button to get Ayurvedic remedy recommendations.", "questionBox-step3"))
        document.getElementById("step3-nextbuttons").style.display = "block";
    }
    else if (index < recommended_symptoms.length) {
        addMessageForQuestion(index);
    }
    else {
        alert("No more questions to ask. Sorry, I am not able to diagnose your disease. 😔");
        location.reload();
    }
}

function handleStepChange(step) {
    console.log(step);
    switch (step) {
        case 1:
            handleStep2();
            break;
        case 2:
            handleStep3();
            break;
        case 3:
            handleStep4();
            break;
    }
}

function handleStep1() {
    addMessageWithTypingEffect("Hello... Welcome to Ayush Health Bot.", "chatboxContent-step1")
    .then(() => addMessageWithTypingEffect("For personalized disease diagnosis and ayurvedic remedy recommendations, firstly please provide me your name, age, and gender." , "chatboxContent-step1"))
    .then(() => addMessageWithTypingEffect(" Thank you! 😊" , "chatboxContent-step1"))
    .then(() => {
        document.getElementById("personal_details").style.display = "block";
        document.getElementById("name").addEventListener("input", function() {
            name = this.value;
            handleNextStep1();
        });
        document.getElementById("age").addEventListener("change", function() {
            age = this.value;
            handleNextStep1();
        });
        document.getElementById("gender").addEventListener("change", function() {
            gender = this.value;
            handleNextStep1();
        });
    });
}

function handleNextStep1() {
    if (name != "" && age != "" && gender != "") {
        document.getElementById("step1-nextbuttons").style.display = "block";
    }
}

function handleStep2() {
    addMessageWithTypingEffect(`Great... ${name}`, "chatboxContent-step2")
    .then(() => addMessageWithTypingEffect("Now, please provide me with the symptoms you are experiencing.", "chatboxContent-step2"))
    .then(() => addMessageWithTypingEffect("You can select multiple symptoms from the autocomplete dropdown. ⬇️", "chatboxContent-step2"))
    .then(() => {
        document.getElementById("symptoms-inputs").style.display = "block";
        let dom_sym = ["sympSelect1", "sympSelect2", "sympSelect3"];
        dom_sym.forEach((sym) => {
            var input = document.getElementById(sym);
            input.addEventListener("input", function() {
                if(symptoms.includes(this.value)){
                    alert(`You have already selected ${this.value} symptom. Select another symptom. 🙏`);
                    this.value = "";
                    return;
                }
                let all_input = Array.from(document.querySelectorAll('.sympt-class-array'),
                ).map((input) => input.value);
                symptoms = all_input.filter((input) => input != "");
                if(symptoms.length == 3)
                    document.getElementById("step2-nextbuttons").style.display = "block";
                else
                    document.getElementById("step2-nextbuttons").style.display = "none";
            });
        });

    });
}

async function handleStep3() {
    await fetchNewSymptoms();

    document.getElementById("chatboxContent-step3").innerHTML = "";
    addMessageWithTypingEffect("Perfect... Based on the your previous symptoms, now I will ask you a few more questions to better understand your condition.", "chatboxContent-step3")
    .then(() => addMessageWithTypingEffect("", "chatboxContent-step3"))
    .then(() => addMessageWithTypingEffect("Note: Answer the following questions with 'YES' or 'NO'.", "chatboxContent-step3"))
    .then(() => {
        document.getElementById("question-inputs").style.display = "block";
        askQuestion(0);
    });
}

async function handleStep4() {
    const res = await fetch("/get_data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({disease: disease[0], age: age, gender: gender}),
    });
    const data = await res.json();
    remedyData = data;

    document.getElementById("chatboxContent-step4").innerHTML = "";
    addMessageWithTypingEffect(`Hey, ${name}! Based on diagnosis, you may have ${fixString(disease[0])}.`, "chatboxContent-step4")
    .then(() => addMessageWithTypingEffect("", "chatboxContent-step4"))
    .then(() => addMessageWithTypingEffect(`Medical condition: ${data.description}`, "chatboxContent-step4"))
    .then(() => addMessageWithTypingEffect("", "chatboxContent-step4"))
    .then(() => addMessageWithTypingEffect("Here are some Ayurvedic remedies for you:", "chatboxContent-step4"))
    .then(async () => {
        for (const remedy of getRele(data.ayurvedicRemedies, Math.min(6, data.ayurvedicRemedies.length))) {
            await addMessageWithTypingEffect(`🌿 ${remedy}`, "chatboxContent-step4");
        }
    }).then(() => {document.getElementById("prompts").style.display = "flex";});
}

document.getElementById("r-yoga").addEventListener("click", function() {
    document.getElementById("r-yoga").style.display = "none";
    document.getElementById("div-r-yoga").style.display = "block";
    addMessageWithTypingEffect("Here are some yoga poses for you:", "chatboxContent-r-yoga")
    .then(async () => {
        for (const yoga of getRele(remedyData.yoga, Math.min(6, remedyData.yoga.length))) {
            await addMessageWithTypingEffect(`🧘 ${yoga}`, "chatboxContent-r-yoga");
        }
    })
});

document.getElementById("r-ayurvedicDiet").addEventListener("click", function() {
    document.getElementById("r-ayurvedicDiet").style.display = "none";
    document.getElementById("div-r-ayurvedicDiet").style.display = "block";
    addMessageWithTypingEffect("Here are some Ayurvedic diet recommendations for you:", "chatboxContent-r-ayurvedicDiet")
    .then(async () => {
        for (const diet of getRele(remedyData.ayurvedicDiet, Math.min(6, remedyData.ayurvedicDiet.length))) {
            await addMessageWithTypingEffect(`🥗 ${diet}`, "chatboxContent-r-ayurvedicDiet");
        }
    })
});

document.getElementById("r-avoidFood").addEventListener("click", function() {
    document.getElementById("r-avoidFood").style.display = "none";
    document.getElementById("div-r-avoidFood").style.display = "block";
    addMessageWithTypingEffect("Here are some foods to avoid:", "chatboxContent-r-avoidFood")
    .then(async () => {
        for (const food of getRele(remedyData.foodAvoid, Math.min(6, remedyData.foodAvoid.length))) {
            await addMessageWithTypingEffect(`❌ ${food}`, "chatboxContent-r-avoidFood");
        }
    })
});

document.getElementById("r-remedy").addEventListener("click", function() {
    document.getElementById("r-remedy").style.display = "none";
    document.getElementById("div-r-remedy").style.display = "block";
    addMessageWithTypingEffect("Here are some Allopathic remedy for you:", "chatboxContent-r-remedy")
    .then(async () => {
        for (const remedy of getRele(remedyData.remedy, Math.min(6, remedyData.remedy.length))) {
            await addMessageWithTypingEffect(`💊 ${remedy}`, "chatboxContent-r-remedy");
        }
    })
});
