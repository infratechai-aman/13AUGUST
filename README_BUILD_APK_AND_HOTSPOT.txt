===========================================================================
SQUAD LEGENDS 3D — ANDROID APK BUILDER & LOCAL HOTSPOT MULTIPLAYER GUIDE
===========================================================================

1. HOW TO GENERATE THE .APK WITHOUT INSTALLING ANDROID STUDIO (2 MINUTES):
   - Upload the contents of this ZIP to a free GitHub repository.
   - Click the "Actions" tab on GitHub -> "Build Squad Legends 3D Android APK".
   - Download "SquadLegends-3D-Android-APK" (app-debug.apk) and install on your Android phone!
   - OR open this folder directly in Android Studio / Website2APK / HopWeb on Android and click "Build APK".

2. HOW TO PLAY MULTIPLAYER ON LOCAL MOBILE HOTSPOT (2 OPTIONS):
   Option A — Pure Offline WebRTC P2P (Inside the Game UI):
     - Connect both phones/laptops to the same Mobile Wi-Fi Hotspot.
     - Open GAME MODES -> Click "📡 Local Hotspot P2P & APK".
     - Player 1 clicks "1. Host: Generate Hotspot Code" and sends the code to Player 2.
     - Player 2 pastes it, clicks "2. Friend: Paste Host Code & Join", and sends the Reply back to Player 1.
     - Both players are now directly linked over Local Wi-Fi Hotspot (< 5ms latency, zero internet needed)!

   Option B — 1-Tap Local Hotspot Python Server (Zero Copy-Paste):
     - Run `python3 start_hotspot_server.py` on PC or Android Termux.
     - Both players open `http://<HOTSPOT_IP>:8080` and enter the same Room Code (e.g. SQ-101)!
