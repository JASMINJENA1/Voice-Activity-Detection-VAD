
# Voice Activity Detection (VAD) Tool

## Overview

The Voice Activity Detection (VAD) Tool is a web application designed to upload audio files, perform voice activity detection (VAD) on them, and display the results. The application is built with React for the front end and FastAPI for the back end. 

## Features

- Upload audio files in WAV format.
- Analyze the audio file for voice activity.
- Display the VAD results on the web interface.

## Project Structure

- **backend/**: Contains the FastAPI server and the VAD processing logic.
- **frontend/**: Contains the React application for the user interface.

## Requirements

- Python 3.7+
- Node.js and npm (or yarn)

## Setup

### Backend

Setting Up the Back-End (FastAPI)
Dependencies:

 ~FastAPI
 ~uvicorn for running the FastAPI server
 ~webrtcvad for VAD processing
 ~pydub for handling audio files
 ~aiofiles for handling file uploads asynchronously

1. Navigate to the Backend Directory:

   [Open bash/cmd]
   mkdir VADProject-backend
    cd VADProject-backend


2. Create and Activate a Virtual Environment:
   [Open bash/cmd and install python3 or above version]    
   python3 -m venv env
   source env/bin/activate  # macOS/Linux
   env\Scripts\activate     # Windows

3. Install Backend Dependencies:
   pip install fastapi uvicorn webrtcvad pydub aiofiles

4. Run the FastAPI Server:
   [bash/cmd]
   uvicorn main:app --reload

   The server will start and be accessible at http://127.0.0.1:8000.

### Frontend

1. Navigate to the Frontend Directory:
   [bash/cmd]
   cd ../frontend

2.  Install Frontend Dependencies: 
       npm install 

3. Start the React Development Server: 
      npm start   

      The React app will be accessible at http://localhost:3000.

### Usage
Open the React application in your browser (http://localhost:3000).
Upload an audio file in WAV format using the file input.
Click the "Upload and Analyze" button.
View the VAD results displayed on the page.  

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

### Contact
For any questions or feedback, please contact jenajasmin0@gmail.com
LinkedIn: https://www.linkedin.com/in/jasmin-jena/

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).


## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


### Contact
For any questions or feedback, please contact jenajasmin0@gmail.com
LinkedIn: https://www.linkedin.com/in/jasmin-jena/






 



