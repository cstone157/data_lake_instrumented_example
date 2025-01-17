const dgram = require('dgram');
//import { createSocket } from 'dgram'

const PORT = process.env.UDP_LISTENER_PORT || 41234
const server = dgram.createSocket('udp4')

server.on('error', (err) => {
  console.error('Listening error:', err)
  server.close()
})

server.on('message', (msg, remoteInfo) => {
  console.log(`Message: ${msg} from ${remoteInfo.address}:${remoteInfo.port}`)
})

server.on('listening', () => {
  const serverAddress = server.address()

  console.log(`Listening at ${serverAddress.address}:${serverAddress.port}`)
})

server.bind(PORT)