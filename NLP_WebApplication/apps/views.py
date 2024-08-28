from django.shortcuts import render, redirect
from . import predict
import logging
from django.shortcuts import render
from django.http import HttpResponseServerError
from . import predict

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'apps/index.html')
    
def summarize(request):
    if request.method == "POST":
        text = request.POST.get("abstract")
        conclude = predict.summarizetext(text)[0]['summary_text']
        return render(request, 'apps/summarize.html', {
            "conclude": conclude,
            "abstract": text,
        })
    return render(request,'apps/summarize.html')

def textgenerator(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        length = int(request.POST.get("length"))
        result = predict.generator(prompt, length)[0]['generated_text']
        return render(request, 'apps/generation.html', {
            "result": result,
            "text": prompt,
        })
    return render(request, 'apps/generation.html')

def qa(request):
    if request.method == "POST":
        question = request.POST.get("question")
        context = request.POST.get("context")
        result = predict.QA(context, question)
        return render(request, 'apps/questions.html',{
            "answer": result[0],
            "score": result[1],
            "question": question,
            "context": context,
        })
    return render(request, 'apps/questions.html')

def sentimental(request):
    if request.method == "POST":
        review = request.POST.get("review")
        logger.info(f"Received review: {review}")
        
        try:
            result = predict.classification(review)
            logger.info(f"Model output: {result}")
            
            # Update the mapping dictionary to match your model's labels
            mapping = {
                'anger': 'Anger',
                'disgust': 'Disgust',
                'fear': 'Fear',
                'joy': 'Joy',
                'neutral': 'Neutral',
                'sadness': 'Sadness',
                'surprise': 'Surprise',
                'optimism': 'Optimism'
            }
            
            label = result[0]['label']
            emotion = mapping.get(label, 'Unknown')
            score = result[0]['score']
            
            logger.info(f"Emotion: {emotion}, Score: {score}")
            
            return render(request, 'apps/sentimental.html', {
                "emotion": emotion,
                "score": round(score, 3),
                "review": review,
            })
        except KeyError as e:
            logger.error(f"KeyError: {e} - Label '{label}' not found in mapping.")
            return HttpResponseServerError(f"Label '{label}' not found in mapping.")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return HttpResponseServerError(f"Unexpected error: {e}")
    
    return render(request, 'apps/sentimental.html')


def translate(request):
    if request.method == "POST":
        text = request.POST.get("text")
        result = predict.translation(text)
        return render(request, 'apps/translate.html',{
            "result": result[0]['translation_text'],
            "text": text,
        })
    return render(request, 'apps/translate.html')


