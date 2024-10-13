// ---------------------------------------------- Functions ----------------------------------------------

// Load JSON file
function loadJSON(jsonFile) {
    return new Promise((resolve, reject) => {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', jsonFile, true);
      xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
          var data = JSON.parse(xhr.responseText);
          resolve(data);
        } else {
          reject('Request failed with status: ' + xhr.status);
        }
      };
      xhr.onerror = function() {
        reject('Request failed');
      };
      xhr.send();
    });
  }

//  JSON to CSV

function jsonToCSV(jsonData) {
    // Extracting unique symptoms
    let symptomsSet = new Set();
    jsonData.forEach(disease => {
        disease.symptom.forEach(symptom => {
            symptomsSet.add(symptom);
        });
    });

    let symptomsList = Array.from(symptomsSet);
    symptomsList = symptomsList.map(symptom => symptom.split(" ").join("_"));

    // Creating CSV header
    let csvContent = symptomsList.join(",")  + ",male,female,infant,child,adult,senior,disease" + "\n";

    jsonData.forEach(disease => {
        let row = [];
        symptomsList.forEach(symptom => {
            if (disease.symptom.includes(symptom.split("_").join(" "))) {
                row.push(1);
            } else {
                row.push(0);
            }
        });

        csvContent += `${row.join(",")},${disease.gender === "male" ? 1 : 0},${disease.gender === "female" ? 1 : 0}`
            + `,${disease.ageGroup === "infant" ? 1 : 0},${disease.ageGroup === "child" ? 1 : 0},${disease.ageGroup === "adult" ? 1 : 0},${disease.ageGroup === "senior" ? 1 : 0},`
            + `${disease.name.split(" ").join("_")}\n`;
    });

    return csvContent;
}

// ---------------------------------------------- Utils ----------------------------------------------

const DisplayPart = document.getElementById('DisplayPart');

// ---------------------------------------------- Main ----------------------------------------------

const Main = async () => {
    try {
        let DisplayContent = 'Display Data Here...';
        const data = await loadJSON('./NewData/NewData.json');
        const herbs = await loadJSON('./NewData/HerbsData.json');

        let contData= {};
        data.forEach((item) => {
            if (contData[item.name]) {
                if(item.gender === "male")
                    ++contData[item.name].male;
                else
                    ++contData[item.name].female;

                if(item.ageGroup === "infant")
                    ++contData[item.name].infant;
                else if(item.ageGroup === "child")
                    ++contData[item.name].child;
                else if(item.ageGroup === "adult")
                    ++contData[item.name].adult;
                else
                    ++contData[item.name].senior;
            } else {
                contData[item.name] = {
                    male: item.gender === "male" ? 1 : 0,
                    female: item.gender === "female"? 1 : 0,
                    infant: item.ageGroup === "infant" ? 1 : 0,
                    child: item.ageGroup === "child" ? 1 : 0,
                    adult: item.ageGroup === "adult" ? 1 : 0,
                    senior: item.ageGroup === "senior" ? 1 : 0
                }
            }
        });

        contData = Object.keys(contData).map((key) => {
            return {
                name: key,
                ...contData[key]
            }
        });

        console.log(contData);
        let symptomsSet = new Set();
        let allSymptoms = 0;
        data.forEach((item) => {
            item.symptom.forEach((symptom) => {
                symptomsSet.add(symptom.toLowerCase());
                ++allSymptoms;
            });
        });

        console.log(Array.from(symptomsSet).sort());
        

        // const csvContent = jsonToCSV(data);
        // console.log(csvContent);


        return;

        let herbsSet = new Set();
        herbs.forEach((item) => {
            herbsSet.add(item.name.toLowerCase());
            herbsSet.add(item.englishName.toLowerCase());
            herbsSet.add(item.hindiName.toLowerCase());
        });
        console.log(herbsSet);
        let dataSet = new Set();
        let cnt1 = 0, cnt2 = 0;
        data.forEach((item) => {
            item.ayurvedicRemedies.forEach((remedy) => {
                dataSet.add(remedy.toLowerCase());
                ++cnt1;
            });
        })
        console.log(dataSet);
        //find partial match of herbs in data
        let commonSet = new Set();
        herbsSet.forEach((item) => {
            dataSet.forEach((dataItem) => {
                if (dataItem.includes(item) || item.includes(dataItem)) {
                    commonSet.add(dataItem);
                    ++cnt2;
                }
            });
        });
        console.log(commonSet);
        console.log(cnt1, cnt2);    
        data.sort((a, b) => {
            if (a.name > b.name) {
                return 1;
            } else if (a.name < b.name) {
                return -1;
            } else 
                a.gender > b.gender ? 1 : -1;
        });
        console.log(data);


        // Display name of unique diseases
        let uniqueDiseases = new Set();
        let c = 0;
        data.forEach((item) => {
            if(uniqueDiseases.has({name: item.name, gender: item.gender, ageGroup: item.ageGroup}))
                ++c;
            else
                uniqueDiseases.add({name: item.name, gender: item.gender, ageGroup: item.ageGroup});
        });


        //sort the uniqueDiseases array
        // uniqueDiseases.sort((a, b) => {
        //     if (a.name > b.name) {
        //         return 1;
        //     } else {
        //         return -1;
        //     }
        // });
        console.log(uniqueDiseases);


        // console all the count of the all fields in data
        let objKeys = Object.keys(data[0]);
        let countObj = {};
        objKeys.forEach((key) => {
            countObj[key] = 0;
        });
        data.forEach((item) => {
            objKeys.forEach((key) => {
                countObj[key] += 1;
            });
        });
        console.log(countObj);


        // convert all the field [name, ageGroup, gender] and symptom array to lowercase
        console.log("lowercase data")
        let newData = [];
        data.forEach((item) => {
            console.log(item.name)
            let newItem = item;
            newItem.name = item.name.toLowerCase();
            newItem.ageGroup = item.ageGroup.toLowerCase();
            newItem.gender = item.gender.toLowerCase();
            newItem.symptom = item.symptom.map((symp) => symp.toLowerCase());
            newData.push(newItem);
        });
        console.log(newData);

        let temp = '';
        newData.forEach((item, index) => {
            temp += `<p> => ${item.name}, ${item.ageGroup}, ${item.gender}<p>`;
        });
        DisplayContent = temp;

        DisplayPart.innerHTML = DisplayContent;
    } catch (error) {
        console.log(error);
    }
}

Main();