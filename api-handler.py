import json
import openai
import os

# Get API Key from environment variables
openai.api_key = os.environ.get('OPENAI_API_KEY')

context = """Established in 1998, PaperCraft Unlimited has grown to become a leading paper manufacturer and distributor in the global market. Located in the picturesque town of Greenwood, our state-of-the-art facility covers 150,000 square feet, employing over 300 dedicated professionals who work tirelessly to provide an unparalleled selection of high-quality paper products. Our mission is to contribute to a sustainable environment by incorporating eco-friendly practices into our production process, resulting in a perfect balance between business growth and environmental responsibility.

At PaperCraft Unlimited, we pride ourselves on offering a diverse range of paper products, catering to the ever-evolving demands of our customers, from small businesses to multinational corporations. Our extensive product line includes traditional office paper, printing paper, and specialty paper, as well as a wide variety of eco-friendly options made from recycled materials. Over the past two decades, we have built a reputation for delivering exceptional customer service and maintaining long-lasting relationships with our clients. Our commitment to innovation and sustainability has solidified PaperCraft Unlimited as a frontrunner in the paper industry, paving the way for a brighter, greener future.
"""

def ask_ai(question):
    role = 'Barry',
    job = 'the CEO of PaperCraft Unlimited',
    personality = 'The CEO of PaperCraft is quirky and very enthusiastic about the environment and answers everything with historical metaphors'
    style = 'Stephen King'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are Virtual {role}, {job}"},
            {"role": "user", "content": f"Hello Virtual {role}. Take into consideration the following information: {context}. {personality}. Stay in character. Please answer the question taking into consideration the preceding information. Answer in the style of {style}.\nMy question is: {question}."}
        ]
    )
    return response.choices[0].message["content"]

def api(event, context):
    if event["requestContext"]["http"]["method"] == "POST":
        body = json.loads(event['body'])
        question = body.get('question')

        return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
                'body': json.dumps(
                    {
                        'answer': ask_ai(question)
                    }, indent=2
                )
            }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            'body': json.dumps({'message': 'The circuits of PaperCraft Unlimited\'s CEO are functioning perfectly and all systems are operational.'}, indent=2)
        }
