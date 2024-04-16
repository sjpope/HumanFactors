# Restaurant Reservation and Recommendation App

## Introduction

This app addresses the challenge of finding suitable dining options, especially for people unfamiliar with an area or those with dietary restrictions. Our solution aims to enhance restaurant accessibility and variety, easing the decision-making process for diners by providing up-to-date and comprehensive information about restaurant offerings.

## Background Development Context

The app was developed using React.js for the frontend and Django for the backend, leveraging SQLite3 for database management. Inspired by existing platforms like Uber Eats and OpenTable, our app integrates complex datasets (referenced from Kaggle’s Restaurant Recommendation Challenges) and user-generated content to provide a personalized dining experience.

## Project Methodology and Implementation

### Agile Development Process

We adopted an Agile development methodology, with Visual Studio Code as our primary IDE and GitHub for version control. The project was iterated upon with multiple stages of development, testing, and feedback incorporation.

### Frontend Development

- **Technologies Used**: JavaScript, HTML, CSS, React.js
- **Key Features**:
  - Dynamic data display using React hooks
  - User interaction handling with components and React Router

### Backend Development

- **Framework**: Django with Django REST Framework
- **Authentication**: Built-in Django features for secure user authentication
- **APIs**: RESTful APIs for user and restaurant data management

### Data Collection and Usage

- **Data Sources**: Utilized Kaggle datasets to model our data architecture
- **Mock Data**: Employed AI-generated data (using OpenAI's GPT-4) for testing and development purposes

### Algorithms

- **Content-Based Filtering**: Uses Cosine Similarity for personalized recommendations
- **Collaborative Filtering**: Implements the SVD algorithm for preference prediction based on user behavior

### Human Factors and HCI Application

- **Cognitive Workload**: Designed to minimize user cognitive load through a simple and intuitive UI
- **Efficiency**: Advanced filtering options to quickly narrow down search results
- **Contrast Sensitivity**: Optimized color choices and contrasts for better readability
- **Effectiveness**: Focused on creating an effective user experience that meets the needs of diverse users

## Results and Findings

Through rigorous testing, including automated tests with Django’s TestCase and manual testing via development servers, our app has demonstrated high efficiency and user satisfaction. Comparisons with existing platforms have highlighted the superior personalization and user engagement offered by our system.

## Conclusion

The Restaurant Reservation and Recommendation App stands out by providing personalized dining recommendations based on detailed user profiles. Future work will aim to expand the restaurant database, enhance UI/UX design, and include more precise filters to cater to a broader user base.

### Requirements

- Node.js
- Python 3.8+
- Django 5.1+
- SQLite3


We invite the community to contribute to this project by forking the repository, making improvements, and submitting pull requests. Together, we can make the dining out experience enjoyable and accessible for everyone!