#!/usr/bin/env python3
"""
Simple HTTP Server for AI Science Teacher
Starts a local web server to run the application
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 8000
HOST = "localhost"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging format
        sys.stdout.write(f"[Server] {format % args}\n")

def main():
    """Start the development server"""
    
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    print("=" * 60)
    print("🌟 Amlak AI Science Teacher - Development Server")
    print("=" * 60)
    print(f"\n📡 Starting server on http://{HOST}:{PORT}")
    print(f"📂 Serving from: {Path.cwd()}")
    print("\n🎯 Access the application at:")
    print(f"   → http://{HOST}:{PORT}/")
    print(f"   → http://127.0.0.1:{PORT}/")
    print("\n⚠️  Press Ctrl+C to stop the server")
    print("=" * 60 + "\n")
    
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            # Open browser automatically
            url = f"http://{HOST}:{PORT}/"
            print(f"🌐 Opening browser to {url}...")
            try:
                webbrowser.open(url)
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"   Please open {url} manually in your browser")
            
            print(f"\n✅ Server is running!\n")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down server...")
        print("👋 Thanks for using AI Science Teacher!\n")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"\n❌ Error: Port {PORT} is already in use!")
            print(f"   Try closing other applications or use a different port")
            print(f"   You can run: python3 start_server.py --port 8001")
        else:
            print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check for custom port in arguments
    if len(sys.argv) > 1:
        try:
            if sys.argv[1] == "--port" and len(sys.argv) > 2:
                PORT = int(sys.argv[2])
            else:
                PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            print("Usage: python3 start_server.py [--port PORT]")
            sys.exit(1)
    
    main()
