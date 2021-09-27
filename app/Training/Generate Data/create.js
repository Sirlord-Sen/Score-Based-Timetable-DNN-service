const createCsvWriter = require('csv-writer').createArrayCsvWriter

// Global Variables
let cwaLimit = [[75, 100], [65, 95], [65, 95], [58, 80], [55, 78], [48, 77], [30, 75], [30, 70], [30, 65], [30, 65]] 
let gpaLimit = [[3.5, 4], [3, 4], [2.5, 4], [2.5, 4], [55, 78], [48, 77], [30, 75], [30, 70], [30, 65], [30, 65]]
let cwaGrades = [[80, 88], [75, 79], [70, 74], [65, 69], [60, 64], [55, 59], [50, 54], [45, 49], [40, 44], [35, 39]] 
let gpaGrades = [[3.9, 4], [3.8, 3.89], [3.6, 3.79], [3.3, 3.59], [3, 3.29], [2.75, 2.99], [2.5, 2.74], [2, 2.49], [1, 1.99], [0.5, 0.99]] 
let studyLimit = [[5, 2], [4.5, 2], [4.25, 1], [4, 1], [3.5, 0.75], [3, 0.5], [2.75, 0.15], [2.25, 0.15], [2, 0], [2, 0]]
let avgStudy = [3, 2.75, 2.25, 1.75, 1.5, 1.25, 1, 0.75, 0.5, 0]
let rate = [0.04, 0.06, 0.09, 0.18, 0.23, 0.16, 0.12, 0.05, 0.03, 0.04]

function GenerateBoundNumbers(lower, upper){
    min = Math.ceil(lower)
    max = Math.floor(upper)
    num = Math.floor(Math.random() * (max - min + 1)) + min
    return num
}

function GenerateStudyHour(cwa, score, diff, avgStudy, studyLimit, weeks){
    let diffAvg = (diff[0][0] + diff[0][1])/2

    function round(value, step){
        step || (step = 1.0);
        var inv = 1.0 / step
        return Math.round(value * inv) / inv
    }
    if(score > cwa && diff[1] > diffAvg){
        num = (Math.random() * (studyLimit[0] - avgStudy)) + avgStudy
        return (round(num, 0.25)) * weeks
    }

    if((score < cwa && (diff[1] <= diffAvg || diff[1] > diffAvg)) || (score > cwa && diff[1] <= diffAvg)){
        num = (Math.random() * (avgStudy - studyLimit[1])) + studyLimit[1]
        return round(num, 0.25) * weeks
    }

    if(score === cwa) return avgStudy * weeks
}

function GenerateCwa(limit, total, rate){
    let cwa = []
    for(let i = 0; i < (total * rate[0]); i ++){
        num = GenerateBoundNumbers(limit[0][0], limit[0][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[1]); i ++){
        num = GenerateBoundNumbers(limit[1][0], limit[1][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[2]); i ++){
        num = GenerateBoundNumbers(limit[2][0], limit[2][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[3]); i ++){
        num = GenerateBoundNumbers(limit[3][0], limit[3][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[4]); i ++){
        num = GenerateBoundNumbers(limit[4][0], limit[4][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[5]); i ++){
        num = GenerateBoundNumbers(limit[5][0], limit[5][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[6]); i ++){
        num = GenerateBoundNumbers(limit[6][0], limit[6][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[7]); i ++){
        num = GenerateBoundNumbers(limit[7][0], limit[7][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[8]); i ++){
        num = GenerateBoundNumbers(limit[8][0], limit[8][1])
        cwa.push(num)
    }
    for(let i = 0; i < (total * rate[9]); i ++){
        num = GenerateBoundNumbers(limit[9][0], limit[9][1])
        cwa.push(num)
    }
    return cwa
}

function GenerateScore(cwaLimit, total, rate){
    let r = 0
    let a = 0
    let tot = 0
    let count = []
    let newcwa = []
    let scores = []
    let newCredits = []
    let difficulty = []
    let studyHour = []
    let tempScore = []
    let tempCwa = []
    let tempDiff = []
    let temphrs = [] 
    let data = []
    

    for (let rat of rate){
        tot = tot + (total * rat)
        count.push(tot);
    }
    let cwaArray = GenerateCwa(cwaGrades, 1000, rate)
    for(let cwa of cwaArray){
        noCourse = GenerateBoundNumbers(6, 12)
        for(let i = 0; i < noCourse; i ++){
            score = GenerateBoundNumbers(cwaLimit[r][0], cwaLimit[r][1])
            diff = GenerateBoundNumbers(1,5)
            hour = GenerateStudyHour(cwa, score, [[1,5], diff], avgStudy[r], studyLimit[r], 15)

            tempDiff.push(diff)
            temphrs.push(hour)
            tempScore.push(score)
            tempCwa.push(cwa)
            
            if(i === (noCourse - 1)){
                var totalCredits = GenerateBoundNumbers(16, 24) 
                var credits = GenerateCredits(noCourse, [1, 4], totalCredits)
                tempScore = GenerateCorrectScores(tempScore, credits, totalCredits, cwa) 

                for(let i in tempCwa){
                    tempData = [tempCwa[i], credits[i], temphrs[i], tempDiff[i], tempScore[i]]
                    data.push(tempData)
                }

                scores.push(...tempScore)
                newcwa.push(...tempCwa)
                newCredits.push(...credits)
                difficulty.push(...tempDiff)
                studyHour.push(...temphrs)
                tempScore = []
                tempCwa = []
                tempDiff = []
                temphrs = []
            }
        } a = a + 1   
        if (a === count[0])  r = r + 1
        if (a === count[1])  r = r + 1
        if (a === count[2])  r = r + 1
        if (a === count[3])  r = r + 1
        if (a === count[4])  r = r + 1
        if (a === count[5])  r = r + 1
        if (a === count[6])  r = r + 1
        if (a === count[7])  r = r + 1
        if (a === count[8])  r = r + 1
        if (a === count[9])  r = r + 1
    }
    
    saveArrayToCSV(data)
}

GenerateScore(cwaLimit, 1000, rate)

function GenerateCorrectScores(scores, credits, totalCredits, cwa){
    swa = (credits.reduce((r, a, i ) => {return r + a*scores[i]}, 0))/ totalCredits
    var diff = Math.round((cwa - swa) * totalCredits)

    if(diff < 0){
        while(diff < 0){
            for(let i = 0; i < scores.length; i++){
                if(diff < 0 && scores[i] > 30){
                    scores[i] --
                    diff = diff + credits[i]
                }
                if (diff >= 0) break
                if (i === (scores.length - 1)) continue
            }
        }
    }
    else if(diff > 0){
        while(diff > 0){
            for(let i = 0; i < scores.length; i++){
                if(diff > 0 && scores[i] <= 100){
                    scores[i] ++
                    diff = diff - credits[i]
                }
                if (diff <= 0) break
                if (i === (scores.length - 1)) continue
            }
        }
    }
        
    return scores
}

function GenerateCredits(n, range , sum){
    var aryRet = [];
    var fSumTmp;
    for (var i = 0; i < n; i++) {
        iTmp = GenerateBoundNumbers(range[0], range[1])
        aryRet.push(iTmp);
    }
    fSumTmp = aryRet.reduce((a,b) => { return a + b; })
    var diff = sum - fSumTmp
    while(diff !== 0){
        for(let i = 0; i < aryRet.length; i++){
            if(diff > 0 && aryRet[i] >= 1 && aryRet[i] < 4){
                aryRet[i] ++
                diff --
            }
            if(diff < 0 && aryRet[i] > 1 && aryRet[i] <= 4){
                aryRet[i] --
                diff ++
            }
            if (diff === 0) break
            if (i === (aryRet.length - 1)) continue
        }
    }
    return aryRet
}


function saveArrayToCSV(data){
    const csvWriter = createCsvWriter({
        header: ["Cwa", "Credits", "Study Hours", "Difficulty", "Scores"],
        path: "data.csv"
    })
    csvWriter.writeRecords(data)
        .then(() => {
            console.log("....Done")
        }) 
}