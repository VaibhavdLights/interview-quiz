import crew

if __name__ == '__main__':
    print('\n---Quiz Maker for Interview Preparations---')
    print('---#####################################---')
    topic=input('Enter the topic ->> ')
    crew.run(inputs={
        'topic': topic,
    })
