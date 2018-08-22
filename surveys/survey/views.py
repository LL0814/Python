from django.shortcuts import render
from django.http import HttpResponse
from survey import models
import json
# Create your views herefrom django.shortcuts import render, redirect

# Create your views here.

def survey(request):
    if request.method == 'GET':
        return render(request, 'surey.html')
    elif request.method == 'POST':
        try:
            result = json.loads(request.body)
            gender = True if result.get('a1') == 'A1' else False
            alimony = int(result.get('a3'))
            models.Result.objects.create(gender=gender, grade=result.get('a2'), alimony=alimony, sourceOfExpense=result.get('a4'),
                                         costType=result.get('a5'), costTypeCount=result.get('a6'), record=result.get('a7'),
                                         plan=result.get('a8'), demand=result.get('a9'), measure=result.get('a10'))
            return HttpResponse("ok")
        except:
            return HttpResponse("error")
    else:
        pass

def result(request):
    results = models.Result.objects.filter().all()
    male,famale = 0,0 #q1
    grade1,grade2,grade3,grade4 = 0,0,0,0 #q2
    alimony1,alimony2,alimony3,alimony4 = 0,0,0,0 #q3
    sourceOfExpense1,sourceOfExpense2,sourceOfExpense3,sourceOfExpense4 = 0,0,0,0 #4
    costType1,costType2,costType3,costType4,costType5,costType6,costType7 = 0,0,0,0,0,0,0 #q5
    costTypeCount1,costTypeCount2,costTypeCount3,costTypeCount4,costTypeCount5,costTypeCount6,costTypeCount7 = 0,0,0,0,0,0,0 #q6
    record1,record2,record3,record4 = 0,0,0,0 #q7
    plan1,plan2,plan3,plan4 = 0,0,0,0 #q8
    demand1,demand2,demand3,demand4 = 0,0,0,0 #q9
    measure1,measure2,measure3,measure4,measure5 = 0,0,0,0,0 #q10
    for result in results:
        #q1
        if result.gender:
            male += 1
        else:
            famale += 1
        #q2
        if result.grade == 'A2':
            grade1 +=1
        elif result.grade == 'B2':
            grade2 +=1
        elif result.grade == 'C2':
            grade3 +=1
        else:
            grade4 +=1
        #q3
        if result.alimony < 0:
            pass
        elif result.alimony <= 1000:
            alimony1 +=1
        elif result.alimony >1000 and result.alimony <=2000:
            alimony2 +=1
        elif result.alimony >2000 and result.alimony <=3000:
            alimony3 +=1
        else:
            alimony4 +=1
        #4
        if 'A4' in result.sourceOfExpense:
            sourceOfExpense1 +=1
        if 'B4' in result.sourceOfExpense:
            sourceOfExpense2 +=1
        if 'C4' in result.sourceOfExpense:
            sourceOfExpense3 +=1
        if 'D4' in result.sourceOfExpense:
            sourceOfExpense4 +=1
        #5
        if 'A5' in result.costType:
            costType1 +=1
        if 'B5' in result.costType:
            costType2 +=1
        if 'C5' in result.costType:
            costType3 +=1
        if 'D5' in result.costType:
            costType4 +=1
        if 'E5' in result.costType:
            costType5 +=1
        if 'F5' in result.costType:
            costType6 +=1
        if 'G5' in result.costType:
            costType7 +=1
        #6
        costTypeCountList = result.costTypeCount.split('/')[1:-1]
        for i in range(len(costTypeCountList)):
            value = int(costTypeCountList[i])
            if i == 0:
                costTypeCount1 += value
            if i == 1:
                costTypeCount2 += value
            if i == 2:
                costTypeCount3 += value
            if i == 3:
                costTypeCount4 += value
            if i == 4:
                costTypeCount5 += value
            if i == 5:
                costTypeCount6 += value
            if i == 6:
                costTypeCount7 += value


        #q7
        if result.record == 'A7':
            record1 +=1
        elif result.record == 'B7':
            record2 +=1
        elif result.record == 'C7':
            record3 +=1
        else:
            record4 +=1
        #q8
        if result.plan == 'A8':
            plan1 +=1
        elif result.plan == 'B8':
            plan2 +=1
        elif result.plan == 'C8':
            plan3 +=1
        else:
            plan4 +=1
        #q9
        if result.demand == 'A9':
            demand1 +=1
        elif result.demand == 'B9':
            demand2 +=1
        elif result.demand == 'C9':
            demand3 +=1
        else:
            demand4 +=1
        #q10
        if result.measure == 'A10':
            measure1 +=1
        elif result.measure == 'B10':
            measure2 +=1
        elif result.measure == 'C10':
            measure3 +=1
        elif result.measure == 'D10':
            measure4 +=1
        else:
            measure5 +=1
        
    a1 = [male,famale]
    a2 = [grade1, grade2, grade3, grade4]
    a3 = [alimony1, alimony2, alimony3, alimony4]
    a4 = [sourceOfExpense1,sourceOfExpense2,sourceOfExpense3,sourceOfExpense4]
    a5 = [costType1,costType2,costType3,costType4,costType5,costType6,costType7]
    a6 = [costTypeCount1,costTypeCount2,costTypeCount3,costTypeCount4,costTypeCount5,costTypeCount6,costTypeCount7]
    a7 = [record1, record2, record3, record4]
    a8 = [plan1, plan2, plan3, plan4]
    a9 = [demand1, demand2, demand3, demand4]
    a10 = [measure1, measure2, measure3, measure4,measure5]
    data = {
        'a1': a1,'a2': a2,'a3': a3, 'a4': a4,'a5': a5,
        'a6': a6,
        'a7': a7,'a8': a8,'a9': a9,'a10': a10,}
    return render(request, 'result.html', data)

def thanks(request):
    return render(request, 'complate.html')