const dgram = require('dgram');
const fs = require('fs');

const PORT = process.env.UDP_LISTENER_PORT || 41234;
const socket = dgram.createSocket('udp4');

const config_path = process.env.CONFIG_FILE_PATH || 'config.json';
const obj = JSON.parse(fs.readFileSync(config_path, 'utf8'));
const log4js = require("log4js");

log4js.configure({
    appenders: { console: { type: "console" } },
    categories: { default: { appenders: ["console"], level: "info" } },
});
const logger = log4js.getLogger();

// Before we start our application, create all of our process (if they don't already exist)
for (let i = 0; i < obj.process.length; i++) {
    if (obj[obj.process[i]] === undefined)
        obj[obj.process[i]] = {};
    obj[obj.process[i]].started = false;
}


// If there is a wait to login the first time
let seconds_to_next_message = 0;
let total_seconds = 0;
if (obj.firstLoginInterval !== undefined) {
    seconds_to_next_message = obj.minFirstLoginInterval + Math.random() * obj.firstLoginInterval;
} else {
    seconds_to_next_message = Math.random() * obj.firstLoginInterval;
}


socket.bind(() => {
    socket.setBroadcast(true);
    const broadcastInterval = setInterval(() => {
        total_seconds++;

        if (total_seconds >= seconds_to_next_message) {
            if (!obj.loggedIn && ((obj.loginOdds !== undefined && obj.loginOdds > Math.random()) || 
                obj.loginOdds === undefined)){
                logMessage('login');
            } else if (obj.logoutOdds !== undefined && obj.loginOdds > Math.random()) {
                // Check to see if we have any processes still running before logging out (I'm pretty sure this will break the graph)
                for (let i=0; i < obj.process.length; i++) {
                    let p = obj.process[i];
                    if (obj[p].started === true){
                        obj[p].started = false;
                        logMessage(p, obj[p].started ? 'Start': 'Stop');
                        
                        // Wait the minimum time and then keep killing processes
                        seconds_to_next_message = seconds_to_next_message + 
                            (obj.minInterval !== undefined) ? (obj.minInterval + Math.random() * obj.interval) : (Math.random() * obj.interval);
                    }
                }
                
                obj.loggedIn = false;
                logMessage('logout')
                  
                // Our or else process messages
            } else { 
                let n = Math.floor(obj.process.length * Math.random());
                let p = obj.process[n]
                if (!obj[p].started){
                    obj[p].started = true;
                } else {
                    obj[p].started = false;
                }
                logMessage(p, obj[p].started ? 'Start': 'Stop');
            }

        }


    }, 1000 * 5)
});

// Log our messages
function logMessage(process, msg) {
    let json = {
        user: obj.user,
        role: obj.role,
        process: process,
        message: msg,
        timestamp: (new Date()).toString()
    };
    
    let toReturn = JSON.stringify(json);
    logger.info(toReturn);
    toReturn = Buffer.from(toReturn);
    
    socket.send(toReturn, 0, toReturn.length, PORT, '255.255.255.255', (err) => {
        if (err) {
            console.error('Broadcast error', err)
            socket.close()
            clearInterval(broadcastInterval)
        }
    })
}
