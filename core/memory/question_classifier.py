class QuestionClassifier:

    MEMORY_QUESTIONS = [

        "what is my",
        "who am i",
        "where do i",
        "which is my",
        "my favourite",
        "my favorite",

    ]

    def is_memory_question(self, question: str):

        question = question.lower()

        for pattern in self.MEMORY_QUESTIONS:

            if pattern in question:
                return True

        return False