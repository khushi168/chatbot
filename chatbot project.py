import random

#dictionary of response rules
response_rules = {
    'hello': ["Hello!", "Hi there!", "Hey!"],
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm just a bot, but thanks for asking!"],
    "name?": ["My name is Chatbot. How can I assist you today?"],
    "what's the weather like today?": ["I'm sorry, I am not equipped with real-time weather information."],
    "what can you do?": ["I can provide information, answer questions, and assist with various tasks."],
    "help": ["Sure, I'm here to help!", "How can I assist you?", "I'm happy to help!"],
    "goodbye": ["Goodbye! Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "what is your age": ["I'm just a chatbot, so I don't have an age!"],
    "tell me a joke": ["Sure! Why don't scientists trust atoms? Because they make up everything!"],
    "what is love": ["I'm just a chatbot, but I appreciate the sentiment!", "Sending virtual love your way!"],
    "do you have any pets?": ["As an AI, I don't have physical form, so I don't have any pets. But I can assist you with pet-related questions!"],
    "tell me something interesting": ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"],
    "what is the capital of india?": ["The capital of India is New Delhi."],
    "what's the largest planet in our solar system?": ["The largest planet in our solar system is Jupiter."],
    "what is the speed of light?": ["The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s)."],
    "name the tallest mountain in the world?": ["Mount Everest is the tallest mountain in the world, reaching a height of 8,848 meters (29,029 feet)."],
    "what is the square root of 144?": ["The square root of 144 is 12."],
    "tell me a fascinating fact about space.": ["Did you know that the Sun makes up 99.86% of the mass in our solar system?"],
    "who painted the mona lisa?": ["The Mona Lisa was painted by Leonardo da Vinci."],
    "name the most populous country in the world?": ["The most populous country in the world is India, with over 1.42 billion people."],
    "who's the current president of united states of america?": ["The current President of the United States of America is Joe Biden, he is the 46th president of USA"],
    "What is artificial intelligence?": ["Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that typically require human intelligence. These tasks include speech recognition, problem-solving, learning, and decision-making."],
    "How does machine learning work?": ["Machine learning is a subset of artificial intelligence where systems learn from data to improve their performance on a specific task. It involves algorithms that enable computers to identify patterns in data and make predictions or decisions without explicit programming."],
    "Explain the concept of the Internet of Things (IoT).": ["The Internet of Things (IoT) is a network of interconnected devices that communicate and exchange data. These devices, which can range from household appliances to industrial machines, are embedded with sensors, software, and other technologies to collect and share information."],
    "What is blockchain technology?": ["Blockchain is a decentralized and distributed ledger technology that records transactions across a network of computers. It ensures transparency, security, and immutability of data by creating a chain of blocks, where each block contains a cryptographic hash of the previous block."],
    "How does virtual reality (VR) differ from augmented reality (AR)?": ["Virtual Reality (VR) immerses users in a completely virtual environment, typically through a headset. Augmented Reality (AR), on the other hand, overlays digital information onto the real world, enhancing the user's perception of the physical environment."],
    "What is the role of a neural network in deep learning?": ["A neural network in deep learning is a computational model inspired by the human brain. It consists of interconnected nodes (neurons) organized into layers. Deep learning uses neural networks with multiple hidden layers to extract and learn complex features from data."],
    "How can businesses benefit from implementing Big Data analytics?": ["Big Data analytics involves the processing and analysis of large and complex datasets to extract valuable insights. Businesses can benefit by making data-driven decisions, identifying patterns and trends, improving efficiency, and gaining a competitive advantage in their respective industries."],
    "default": ["I'm sorry, I don't understand. Can you please rephrase your question?"]
}


#function to process user input and generate a response
def get_response(input_text):
    input_text = input_text.lower()

    for key, values in response_rules.items():
        if key in input_text:
            return random.choice(values)

    return random.choice(response_rules['default'])


# Main loop for the chatbot
def main():
    print("ChatBot: Hi, how can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break

        response = get_response(user_input)
        print("ChatBot:", response)


if __name__ == "__main__":
    main()
