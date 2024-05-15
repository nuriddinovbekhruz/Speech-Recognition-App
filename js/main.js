// main.js
const { app, BrowserWindow, ipcMain} = require('electron');
const { spawn } =  require('child_process');
let mainWindow;
function createWindow() {
  // Create the browser window
  mainWindow = new BrowserWindow({
    width: 350,
    height: 600,
    maxWidth: 400,
    maxHeight: 650,
    resizable: false,
    maximizable: false,
    webPreferences: {
      nodeIntegration: true, // enable Node.js integration
      contextIsolation: false
      }
  });

  // Load your HTML file
  mainWindow.loadFile('html/main.html');
}

// When Electron has finished initialization and is ready to create browser windows
app.whenReady().then(createWindow);

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

// Handle audio data received from frontend
ipcMain.on('audio-data', function (event, dataTranslate) {

  // Before npm start check you are in virtual env of python 
  const pythonProcess = spawn('python', ['home.py']); 
  // // Send audio data to Python
  pythonProcess.stdin.write(JSON.stringify(dataTranslate));
  pythonProcess.stdin.end();

  // Receive data from Python
  pythonProcess.stdout.on('data', function (data) {
    // Send the result back to the frontend
    mainWindow.webContents.send('result', data.toString());
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Error executing Python function: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python function execution complete with code ${code}`);
  });

});