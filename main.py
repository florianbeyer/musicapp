from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone
import httpx

app = FastAPI(
    title="Music App API",
    description="A minimalistic FastAPI application with health endpoint and Deezer music search",
    version="1.0.0"
)

# HTTP client for making requests to Deezer API
http_client = httpx.AsyncClient(timeout=10.0)


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint that returns a psychedelic music search interface.
    
    Returns:
        HTMLResponse: An interactive music search page
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>crazy musix explorer</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            @keyframes gradientShift {
                0% { background-position: 0% 0%; }
                25% { background-position: 100% 0%; }
                50% { background-position: 100% 100%; }
                75% { background-position: 0% 100%; }
                100% { background-position: 0% 0%; }
            }
            
            @keyframes crazyFloat {
                0% { transform: translateY(0px) rotate(0deg) scale(1); }
                25% { transform: translateY(-15px) rotate(3deg) scale(1.02); }
                50% { transform: translateY(0px) rotate(-3deg) scale(0.98); }
                75% { transform: translateY(15px) rotate(5deg) scale(1.01); }
                100% { transform: translateY(0px) rotate(0deg) scale(1); }
            }
            
            @keyframes extremePulse {
                0%, 100% { transform: scale(1) rotate(0deg); }
                50% { transform: scale(1.05) rotate(2deg); }
            }
            
            @keyframes rainbowGlow {
                0% { box-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000, 0 0 60px #ff0000; filter: hue-rotate(0deg); }
                25% { box-shadow: 0 0 20px #00ff00, 0 0 40px #00ff00, 0 0 60px #00ff00; filter: hue-rotate(90deg); }
                50% { box-shadow: 0 0 20px #0000ff, 0 0 40px #0000ff, 0 0 60px #0000ff; filter: hue-rotate(180deg); }
                75% { box-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff, 0 0 60px #ff00ff; filter: hue-rotate(270deg); }
                100% { box-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000, 0 0 60px #ff0000; filter: hue-rotate(360deg); }
            }
            
            @keyframes wildSlide {
                from {
                    opacity: 0;
                    transform: translateX(-50px) rotate(-10deg) scale(0.95);
                }
                to {
                    opacity: 1;
                    transform: translateX(0) rotate(0deg) scale(1);
                }
            }
            
            @keyframes crazySpinZoom {
                0% { transform: rotate(0deg) scale(1); }
                50% { transform: rotate(180deg) scale(1.1); }
                100% { transform: rotate(360deg) scale(1); }
            }
            
            @keyframes extremeGlitch {
                0% { transform: translate(0) skew(0deg); filter: hue-rotate(0deg); }
                10% { transform: translate(-3px, 2px) skew(1deg); filter: hue-rotate(90deg); }
                20% { transform: translate(3px, -2px) skew(-1deg); filter: hue-rotate(180deg); }
                30% { transform: translate(-2px, 3px) skew(2deg); filter: hue-rotate(270deg); }
                40% { transform: translate(2px, -3px) skew(-2deg); filter: hue-rotate(360deg); }
                50% { transform: translate(0) skew(0deg); filter: hue-rotate(0deg); }
                60% { transform: translate(3px, 3px) skew(1deg); filter: hue-rotate(90deg); }
                70% { transform: translate(-3px, -3px) skew(-1deg); filter: hue-rotate(180deg); }
                80% { transform: translate(2px, -2px) skew(1deg); filter: hue-rotate(270deg); }
                90% { transform: translate(-2px, 2px) skew(-1deg); filter: hue-rotate(360deg); }
                100% { transform: translate(0) skew(0deg); filter: hue-rotate(0deg); }
            }
            
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                10% { transform: translateX(-3px) rotate(-1deg); }
                20% { transform: translateX(3px) rotate(1deg); }
                30% { transform: translateX(-3px) rotate(-1deg); }
                40% { transform: translateX(3px) rotate(1deg); }
                50% { transform: translateX(-3px) rotate(-1deg); }
                60% { transform: translateX(3px) rotate(1deg); }
                70% { transform: translateX(-3px) rotate(-1deg); }
                80% { transform: translateX(3px) rotate(1deg); }
                90% { transform: translateX(-3px) rotate(-1deg); }
            }
            
            @keyframes bounce {
                0%, 100% { transform: translateY(0) scaleY(1); }
                50% { transform: translateY(-20px) scaleY(1.05); }
            }
            
            @keyframes colorShift {
                0% { filter: hue-rotate(0deg) saturate(1.5); }
                100% { filter: hue-rotate(360deg) saturate(1.5); }
            }
            
            @keyframes wiggle {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(5deg); }
                75% { transform: rotate(-5deg); }
            }
            
            @keyframes bombShake {
                0%, 100% { transform: translate(0, 0) rotate(0deg); }
                10% { transform: translate(-5px, -5px) rotate(-5deg); }
                20% { transform: translate(5px, -5px) rotate(5deg); }
                30% { transform: translate(-5px, 5px) rotate(-5deg); }
                40% { transform: translate(5px, 5px) rotate(5deg); }
                50% { transform: translate(-5px, -5px) rotate(-5deg); }
                60% { transform: translate(5px, -5px) rotate(5deg); }
                70% { transform: translate(-5px, 5px) rotate(-5deg); }
                80% { transform: translate(5px, 5px) rotate(5deg); }
                90% { transform: translate(-5px, 0) rotate(-5deg); }
            }
            
            @keyframes bombExplode {
                0% {
                    transform: scale(1);
                    opacity: 1;
                }
                50% {
                    transform: scale(1.3);
                    opacity: 0.8;
                    filter: brightness(2) hue-rotate(180deg);
                }
                100% {
                    transform: scale(1.5);
                    opacity: 0;
                    filter: brightness(3) hue-rotate(360deg);
                }
            }
            
            @keyframes bombPulse {
                0%, 100% {
                    transform: scale(1);
                    filter: drop-shadow(0 0 10px #ff0000);
                }
                50% {
                    transform: scale(1.1);
                    filter: drop-shadow(0 0 30px #ff6600) drop-shadow(0 0 50px #ffff00);
                }
            }
            
            @keyframes blackHoleSuck {
                0% {
                    transform: scale(1) rotate(0deg) perspective(1000px) rotateX(0deg) rotateY(0deg);
                    opacity: 1;
                    filter: brightness(1) contrast(1) saturate(1) hue-rotate(0deg) blur(0px);
                }
                25% {
                    transform: scale(0.8) rotate(360deg) perspective(1000px) rotateX(45deg) rotateY(45deg);
                    opacity: 0.9;
                    filter: brightness(1.5) contrast(2) saturate(3) hue-rotate(90deg) blur(2px);
                }
                50% {
                    transform: scale(0.4) rotate(900deg) perspective(1000px) rotateX(90deg) rotateY(180deg);
                    opacity: 0.5;
                    filter: brightness(0.3) contrast(5) saturate(5) hue-rotate(180deg) blur(5px);
                }
                75% {
                    transform: scale(0.1) rotate(1440deg) perspective(1000px) rotateX(180deg) rotateY(360deg);
                    opacity: 0.2;
                    filter: brightness(0.1) contrast(10) saturate(10) hue-rotate(270deg) blur(10px);
                }
                100% {
                    transform: scale(0) rotate(2160deg) perspective(1000px) rotateX(360deg) rotateY(720deg);
                    opacity: 0;
                    filter: brightness(0) contrast(20) saturate(0) hue-rotate(360deg) blur(20px);
                }
            }
            
            @keyframes unicornRide {
                0% {
                    transform: scale(0) translateX(-300%) translateY(200%) rotate(-720deg) perspective(2000px) rotateX(-180deg) rotateY(-360deg);
                    opacity: 0;
                    filter: brightness(0) hue-rotate(0deg) saturate(0) contrast(0) blur(30px);
                }
                20% {
                    transform: scale(0.5) translateX(-150%) translateY(100%) rotate(-360deg) perspective(2000px) rotateX(-90deg) rotateY(-180deg);
                    opacity: 0.5;
                    filter: brightness(2) hue-rotate(72deg) saturate(5) contrast(3) blur(15px);
                }
                40% {
                    transform: scale(1) translateX(-50%) translateY(50%) rotate(-180deg) perspective(2000px) rotateX(-45deg) rotateY(-90deg);
                    opacity: 0.8;
                    filter: brightness(3) hue-rotate(144deg) saturate(8) contrast(5) blur(8px);
                }
                60% {
                    transform: scale(1.3) translateX(20%) translateY(-20%) rotate(90deg) perspective(2000px) rotateX(45deg) rotateY(90deg);
                    opacity: 1;
                    filter: brightness(4) hue-rotate(216deg) saturate(10) contrast(7) blur(3px);
                }
                80% {
                    transform: scale(1.1) translateX(10%) translateY(-10%) rotate(45deg) perspective(2000px) rotateX(20deg) rotateY(45deg);
                    opacity: 1;
                    filter: brightness(2.5) hue-rotate(288deg) saturate(6) contrast(4) blur(1px);
                }
                100% {
                    transform: scale(1) translateX(0) translateY(0) rotate(0deg) perspective(2000px) rotateX(0deg) rotateY(0deg);
                    opacity: 1;
                    filter: brightness(1) hue-rotate(360deg) saturate(1.5) contrast(1) blur(0px);
                }
            }
            
            @keyframes blackHoleVortex {
                0% {
                    transform: scale(0) rotate(0deg);
                    opacity: 0;
                    box-shadow: 0 0 0 rgba(0, 0, 0, 0);
                    filter: blur(0px) brightness(1);
                }
                25% {
                    transform: scale(2) rotate(360deg);
                    opacity: 0.8;
                    box-shadow: 0 0 100px rgba(138, 43, 226, 0.8), 0 0 200px rgba(75, 0, 130, 0.6), inset 0 0 100px rgba(0, 0, 0, 0.9);
                    filter: blur(5px) brightness(0.5);
                }
                50% {
                    transform: scale(5) rotate(900deg);
                    opacity: 1;
                    box-shadow: 0 0 200px rgba(138, 43, 226, 1), 0 0 400px rgba(75, 0, 130, 0.8), 0 0 600px rgba(25, 0, 51, 0.6), inset 0 0 200px rgba(0, 0, 0, 1);
                    filter: blur(10px) brightness(0.2);
                }
                75% {
                    transform: scale(3) rotate(1440deg);
                    opacity: 0.6;
                    box-shadow: 0 0 150px rgba(138, 43, 226, 0.8), 0 0 300px rgba(75, 0, 130, 0.6), inset 0 0 150px rgba(0, 0, 0, 0.9);
                    filter: blur(8px) brightness(0.3);
                }
                100% {
                    transform: scale(0) rotate(2160deg);
                    opacity: 0;
                    box-shadow: 0 0 0 rgba(0, 0, 0, 0);
                    filter: blur(20px) brightness(0);
                }
            }
            
            @keyframes unicornGallop {
                0% {
                    transform: translateY(0) rotate(0deg) scale(1);
                    filter: drop-shadow(0 0 30px rgba(255, 0, 255, 0.8));
                }
                10% {
                    transform: translateY(-40px) rotate(15deg) scale(1.1);
                    filter: drop-shadow(0 0 50px rgba(255, 0, 0, 1)) drop-shadow(0 0 80px rgba(255, 127, 0, 0.8));
                }
                20% {
                    transform: translateY(-20px) rotate(-10deg) scale(0.95);
                    filter: drop-shadow(0 0 50px rgba(255, 255, 0, 1)) drop-shadow(0 0 80px rgba(0, 255, 0, 0.8));
                }
                30% {
                    transform: translateY(-50px) rotate(20deg) scale(1.15);
                    filter: drop-shadow(0 0 50px rgba(0, 255, 255, 1)) drop-shadow(0 0 80px rgba(0, 0, 255, 0.8));
                }
                40% {
                    transform: translateY(-10px) rotate(-15deg) scale(0.9);
                    filter: drop-shadow(0 0 50px rgba(75, 0, 130, 1)) drop-shadow(0 0 80px rgba(148, 0, 211, 0.8));
                }
                50% {
                    transform: translateY(-60px) rotate(25deg) scale(1.2);
                    filter: drop-shadow(0 0 60px rgba(255, 0, 255, 1)) drop-shadow(0 0 100px rgba(255, 0, 127, 0.9));
                }
                60% {
                    transform: translateY(-30px) rotate(-20deg) scale(1.05);
                    filter: drop-shadow(0 0 50px rgba(255, 127, 0, 1)) drop-shadow(0 0 80px rgba(255, 255, 0, 0.8));
                }
                70% {
                    transform: translateY(-45px) rotate(18deg) scale(1.1);
                    filter: drop-shadow(0 0 50px rgba(0, 255, 0, 1)) drop-shadow(0 0 80px rgba(0, 255, 255, 0.8));
                }
                80% {
                    transform: translateY(-15px) rotate(-12deg) scale(0.98);
                    filter: drop-shadow(0 0 50px rgba(0, 0, 255, 1)) drop-shadow(0 0 80px rgba(75, 0, 130, 0.8));
                }
                90% {
                    transform: translateY(-35px) rotate(10deg) scale(1.08);
                    filter: drop-shadow(0 0 50px rgba(148, 0, 211, 1)) drop-shadow(0 0 80px rgba(255, 0, 255, 0.8));
                }
                100% {
                    transform: translateY(0) rotate(0deg) scale(1);
                    filter: drop-shadow(0 0 40px rgba(255, 0, 255, 0.9)) drop-shadow(0 0 70px rgba(255, 127, 255, 0.7));
                }
            }
            
            @keyframes rainbowTrail {
                0% {
                    opacity: 0;
                    transform: translateX(-200px) scale(0.5) rotate(-45deg);
                    filter: blur(20px) brightness(0);
                }
                20% {
                    opacity: 0.8;
                    transform: translateX(-100px) scale(1.2) rotate(-20deg);
                    filter: blur(10px) brightness(2) saturate(5);
                }
                40% {
                    opacity: 1;
                    transform: translateX(0) scale(1.5) rotate(0deg);
                    filter: blur(5px) brightness(3) saturate(8);
                }
                60% {
                    opacity: 1;
                    transform: translateX(50px) scale(1.3) rotate(10deg);
                    filter: blur(8px) brightness(2.5) saturate(6);
                }
                80% {
                    opacity: 0.6;
                    transform: translateX(150px) scale(1) rotate(30deg);
                    filter: blur(15px) brightness(1.5) saturate(3);
                }
                100% {
                    opacity: 0;
                    transform: translateX(300px) scale(0.5) rotate(45deg);
                    filter: blur(25px) brightness(0);
                }
            }
            
            @keyframes sparkleExplosion {
                0% {
                    transform: scale(0) rotate(0deg);
                    opacity: 0;
                }
                50% {
                    transform: scale(3) rotate(180deg);
                    opacity: 1;
                }
                100% {
                    transform: scale(5) rotate(360deg);
                    opacity: 0;
                }
            }
            
            body.black-hole-active .container {
                animation: blackHoleSuck 2s ease-in forwards;
            }
            
            body.unicorn-return .container {
                animation: unicornRide 2s ease-out forwards;
            }
            
            .black-hole-overlay {
                position: fixed;
                top: 50%;
                left: 50%;
                width: 100px;
                height: 100px;
                transform: translate(-50%, -50%);
                background: radial-gradient(circle, #000000 0%, #1a0033 30%, #330066 60%, transparent 100%);
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
                opacity: 0;
            }
            
            body.black-hole-active .black-hole-overlay {
                animation: blackHoleVortex 2s ease-in-out forwards;
            }
            
            .unicorn-overlay {
                position: fixed;
                bottom: -200px;
                left: -200px;
                font-size: 20rem;
                z-index: 9998;
                opacity: 0;
                pointer-events: none;
                filter: drop-shadow(0 0 30px rgba(255, 0, 255, 0.8));
            }
            
            .unicorn-overlay::before {
                content: '✨';
                position: absolute;
                font-size: 5rem;
                animation: sparkleExplosion 1s infinite;
            }
            
            .unicorn-overlay::after {
                content: '⭐💫🌟✨🌈';
                position: absolute;
                font-size: 3rem;
                white-space: nowrap;
                animation: sparkleExplosion 1.5s infinite reverse;
            }
            
            body.unicorn-return .unicorn-overlay {
                animation: unicornGallop 2s ease-out forwards;
                opacity: 1;
                bottom: 20%;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .rainbow-trail {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 9997;
                opacity: 0;
            }
            
            body.unicorn-return .rainbow-trail {
                background:
                    repeating-linear-gradient(90deg,
                        transparent 0%,
                        rgba(255, 0, 0, 0.6) 5%,
                        rgba(255, 127, 0, 0.6) 10%,
                        rgba(255, 255, 0, 0.6) 15%,
                        rgba(0, 255, 0, 0.6) 20%,
                        rgba(0, 255, 255, 0.6) 25%,
                        rgba(0, 0, 255, 0.6) 30%,
                        rgba(75, 0, 130, 0.6) 35%,
                        rgba(148, 0, 211, 0.6) 40%,
                        rgba(255, 0, 255, 0.6) 45%,
                        transparent 50%),
                    radial-gradient(circle at 30% 50%, rgba(255, 255, 0, 0.4) 0%, transparent 50%),
                    radial-gradient(circle at 70% 50%, rgba(255, 0, 255, 0.4) 0%, transparent 50%),
                    radial-gradient(circle at 50% 30%, rgba(0, 255, 255, 0.4) 0%, transparent 50%);
                animation: rainbowTrail 2s ease-out forwards;
                box-shadow: inset 0 0 100px rgba(255, 255, 255, 0.5);
            }
            
            body {
                font-family: 'Comic Sans MS', 'Courier New', monospace;
                min-height: 100vh;
                background: linear-gradient(-45deg, #ff00de, #00fff2, #ff6b00, #00ff88, #8000ff, #ff0000, #ffff00, #00ff00, #0000ff);
                background-size: 800% 800%;
                animation: gradientShift 20s ease infinite;
                color: white;
                overflow-x: hidden;
                position: relative;
            }
            
            body::before {
                content: '🎵🎸🎹🎤🎧🎼🎺🎷🥁';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                font-size: 5rem;
                opacity: 0.1;
                animation: crazySpinZoom 30s infinite, colorShift 15s infinite;
                pointer-events: none;
                z-index: 1;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                align-items: center;
            }
            
            body::after {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 200%;
                height: 200%;
                background:
                    radial-gradient(circle at 20% 50%, rgba(255, 0, 222, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(0, 255, 242, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 50% 20%, rgba(255, 107, 0, 0.3) 0%, transparent 50%),
                    radial-gradient(circle at 50% 80%, rgba(128, 0, 255, 0.3) 0%, transparent 50%);
                animation: crazySpinZoom 60s infinite reverse;
                pointer-events: none;
                z-index: 1;
            }
            
            .magic-button {
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                padding: 1.5rem 3rem;
                font-size: 1.5rem;
                font-weight: bold;
                background: linear-gradient(135deg, #ff00de, #00fff2, #ff6b00, #8000ff);
                background-size: 300% 300%;
                border: 4px solid white;
                border-radius: 50px;
                color: white;
                cursor: pointer;
                z-index: 1000;
                animation: extremePulse 2s infinite, gradientShift 5s infinite;
                text-transform: uppercase;
                letter-spacing: 0.2rem;
                box-shadow: 0 0 30px rgba(255, 0, 222, 0.8), 0 0 60px rgba(0, 255, 242, 0.6);
                transition: all 0.3s;
            }
            
            .magic-button:hover {
                transform: translateX(-50%) scale(1.1) rotate(5deg);
                animation: wiggle 0.5s infinite, rainbowGlow 2s infinite;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                position: relative;
                z-index: 2;
            }
            
            .header {
                text-align: center;
                margin-bottom: 3rem;
                animation: crazyFloat 8s ease-in-out infinite;
                transform-origin: center;
            }
            
            h1 {
                font-size: 5rem;
                font-weight: 900;
                text-transform: uppercase;
                letter-spacing: 0.5rem;
                background: linear-gradient(45deg, #ff00de, #00fff2, #ff6b00, #00ff88, #8000ff, #ff0000);
                background-size: 300% 300%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: extremeGlitch 5s infinite, gradientShift 10s infinite, bounce 3s infinite;
                margin-bottom: 0.5rem;
                filter: drop-shadow(0 0 30px #ff00de) drop-shadow(0 0 60px #00fff2);
                transform-style: preserve-3d;
            }
            
            h1:hover {
                animation: extremeGlitch 2s infinite, wiggle 2s infinite, extremePulse 2s infinite;
            }
            
            .subtitle {
                font-size: 1.5rem;
                color: #fff;
                text-shadow: 0 0 20px rgba(0, 255, 242, 1), 0 0 40px rgba(255, 0, 222, 1);
                letter-spacing: 0.3rem;
                animation: colorShift 10s infinite, extremePulse 4s infinite;
                font-weight: bold;
            }
            
            .help-btn {
                position: fixed;
                bottom: 30px;
                left: 20px;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                background: linear-gradient(135deg, #ff00de, #00fff2, #ff6b00, #8000ff);
                background-size: 300% 300%;
                border: 5px solid white;
                color: white;
                font-size: 2.5rem;
                cursor: pointer;
                z-index: 1000;
                animation: extremePulse 3s infinite, rainbowGlow 6s infinite, gradientShift 10s infinite;
                transition: all 0.5s;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
            }
            
            .help-btn:hover {
                transform: scale(1.2) rotate(15deg);
                animation: wiggle 1s infinite, extremePulse 1s infinite;
            }
            
            .info-btn {
                position: fixed;
                bottom: 30px;
                left: 110px;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                background: linear-gradient(135deg, #8000ff, #ff6b00, #00fff2, #ff00de);
                background-size: 300% 300%;
                border: 5px solid white;
                color: white;
                font-size: 2.5rem;
                cursor: pointer;
                z-index: 1000;
                animation: extremePulse 3s infinite reverse, rainbowGlow 6s infinite reverse, gradientShift 10s infinite reverse;
                transition: all 0.5s;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
            }
            
            .info-btn:hover {
                transform: scale(1.2) rotate(-15deg);
                animation: wiggle 1s infinite reverse, extremePulse 1s infinite;
            }
            
            .lang-btn {
                position: fixed;
                bottom: 30px;
                left: 200px;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                background: linear-gradient(135deg, #00ff88, #00fff2, #ff6b00, #ff00de);
                background-size: 300% 300%;
                border: 5px solid white;
                color: white;
                font-size: 1.8rem;
                cursor: pointer;
                z-index: 1000;
                animation: extremePulse 3s infinite, rainbowGlow 6s infinite, gradientShift 10s infinite;
                transition: all 0.5s;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
            }
            
            .lang-btn:hover {
                transform: scale(1.2) rotate(10deg);
                animation: wiggle 1s infinite, extremePulse 1s infinite;
            }
            
            .help-modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                z-index: 999;
                align-items: center;
                justify-content: center;
            }
            
            .help-modal.active {
                display: flex;
            }
            
            .help-content {
                background: linear-gradient(135deg, #1a1a2e, #16213e);
                padding: 2rem;
                border-radius: 20px;
                max-width: 500px;
                border: 3px solid #00fff2;
                box-shadow: 0 0 50px rgba(0, 255, 242, 0.5);
                animation: slideIn 0.5s ease;
            }
            
            .help-content h2 {
                color: #ff00de;
                margin-bottom: 1rem;
                font-size: 2rem;
            }
            
            .help-content p {
                margin-bottom: 1rem;
                line-height: 1.6;
            }
            
            .close-btn {
                background: #ff00de;
                border: none;
                color: white;
                padding: 0.75rem 2rem;
                border-radius: 25px;
                cursor: pointer;
                font-size: 1rem;
                font-weight: bold;
                margin-top: 1rem;
                transition: all 0.3s;
            }
            
            .close-btn:hover {
                background: #00fff2;
                transform: scale(1.05);
            }
            
            .info-modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.85);
                z-index: 999;
                align-items: center;
                justify-content: center;
            }
            
            .info-modal.active {
                display: flex;
            }
            
            .info-content {
                background: linear-gradient(135deg, #2e1a4e, #3e1642);
                padding: 2.5rem;
                border-radius: 25px;
                max-width: 600px;
                border: 4px solid #8000ff;
                box-shadow: 0 0 60px rgba(128, 0, 255, 0.6), 0 0 100px rgba(255, 0, 222, 0.4);
                animation: slideIn 0.5s ease, pulse 3s infinite;
                max-height: 80vh;
                overflow-y: auto;
            }
            
            .info-content h2 {
                color: #ff00de;
                margin-bottom: 1.5rem;
                font-size: 2.5rem;
                text-align: center;
                text-shadow: 0 0 20px rgba(255, 0, 222, 0.8);
            }
            
            .info-content h3 {
                color: #00fff2;
                margin-top: 1.5rem;
                margin-bottom: 1rem;
                font-size: 1.5rem;
                text-shadow: 0 0 15px rgba(0, 255, 242, 0.8);
            }
            
            .info-content p, .info-content li {
                margin-bottom: 1rem;
                line-height: 1.8;
                font-size: 1.05rem;
            }
            
            .info-content ul {
                margin-left: 1.5rem;
                margin-bottom: 1rem;
            }
            
            .ai-badge {
                background: linear-gradient(135deg, #ff00de, #8000ff);
                padding: 0.5rem 1rem;
                border-radius: 15px;
                display: inline-block;
                margin: 1rem 0;
                font-weight: bold;
                animation: pulse 2s infinite;
                box-shadow: 0 0 20px rgba(255, 0, 222, 0.6);
            }
            
            .disclaimer-box {
                background: rgba(255, 107, 0, 0.2);
                border-left: 4px solid #ff6b00;
                padding: 1rem;
                margin: 1rem 0;
                border-radius: 10px;
            }
            
            .search-container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 2rem;
                border-radius: 30px;
                border: 3px solid rgba(255, 255, 255, 0.3);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                margin-bottom: 3rem;
            }
            
            .search-form {
                display: flex;
                gap: 1rem;
                flex-wrap: wrap;
            }
            
            #searchInput {
                flex: 1;
                min-width: 250px;
                padding: 1.2rem 1.5rem;
                font-size: 1.2rem;
                border: 3px solid #00fff2;
                border-radius: 50px;
                background: rgba(0, 0, 0, 0.5);
                color: white;
                outline: none;
                transition: all 0.3s;
                font-family: 'Courier New', monospace;
            }
            
            #searchInput:focus {
                border-color: #ff00de;
                box-shadow: 0 0 20px rgba(255, 0, 222, 0.5);
                transform: scale(1.02);
            }
            
            #searchInput::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }
            
            #searchBtn {
                padding: 1.2rem 3rem;
                font-size: 1.2rem;
                font-weight: bold;
                border: none;
                border-radius: 50px;
                background: linear-gradient(135deg, #ff00de, #ff6b00);
                color: white;
                cursor: pointer;
                transition: all 0.3s;
                text-transform: uppercase;
                letter-spacing: 0.1rem;
                animation: pulse 2s infinite;
            }
            
            #searchBtn:hover {
                transform: scale(1.05) rotate(-2deg);
                box-shadow: 0 0 30px rgba(255, 0, 222, 0.8);
            }
            
            #searchBtn:active {
                transform: scale(0.95);
            }
            
            .loading {
                text-align: center;
                padding: 3rem;
                display: none;
            }
            
            .loading.active {
                display: block;
            }
            
            .spinner {
                width: 80px;
                height: 80px;
                border: 8px solid rgba(255, 255, 255, 0.2);
                border-top: 8px solid #ff00de;
                border-radius: 50%;
                margin: 0 auto 1rem;
                animation: spin 1s linear infinite;
            }
            
            .loading-text {
                font-size: 1.5rem;
                color: #00fff2;
                text-shadow: 0 0 10px rgba(0, 255, 242, 0.8);
                animation: pulse 1s infinite;
            }
            
            .error {
                background: rgba(255, 0, 0, 0.2);
                border: 2px solid #ff0000;
                padding: 1.5rem;
                border-radius: 15px;
                margin-bottom: 2rem;
                display: none;
                animation: slideIn 0.5s ease;
            }
            
            .error.active {
                display: block;
            }
            
            .error-text {
                color: #ff6b6b;
                font-size: 1.1rem;
            }
            
            .results {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                gap: 2rem;
            }
            
            .result-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                overflow: hidden;
                border: 2px solid rgba(255, 255, 255, 0.2);
                transition: all 0.3s;
                animation: slideIn 0.5s ease;
                cursor: pointer;
            }
            
            .result-card:hover {
                animation: bombShake 0.5s ease-in-out;
                border-color: #ff0000;
                box-shadow: 0 10px 40px rgba(255, 0, 0, 0.8), 0 0 60px rgba(255, 102, 0, 0.6);
                position: relative;
            }
            
            .result-card:hover::before {
                content: '💣';
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 8rem;
                z-index: 10;
                animation: bombPulse 0.5s ease-in-out, bombExplode 0.8s ease-out 0.5s forwards;
                pointer-events: none;
            }
            
            .result-card:hover::after {
                content: '💥';
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 12rem;
                z-index: 9;
                opacity: 0;
                animation: bombExplode 0.6s ease-out 1.3s forwards;
                pointer-events: none;
            }
            
            .result-card img {
                width: 100%;
                height: 280px;
                object-fit: cover;
                transition: transform 0.3s;
            }
            
            .result-card:hover img {
                transform: scale(1.1);
            }
            
            .result-info {
                padding: 2rem;
                animation: colorShift 10s infinite;
            }
            
            .result-title {
                font-size: 1.5rem;
                font-weight: 900;
                color: #00fff2;
                margin-bottom: 0.5rem;
                text-shadow: 0 0 20px rgba(0, 255, 242, 1), 0 0 40px rgba(255, 0, 222, 1);
                animation: extremePulse 4s infinite, bounce 5s infinite;
                text-transform: uppercase;
            }
            
            .result-artist {
                font-size: 1.3rem;
                font-weight: bold;
                color: #ff00de;
                text-shadow: 0 0 20px rgba(255, 0, 222, 1), 0 0 40px rgba(0, 255, 242, 1);
                animation: wiggle 4s infinite, colorShift 10s infinite;
            }
            
            .audio-controls {
                padding: 1rem;
                display: flex;
                align-items: center;
                gap: 1rem;
                background: rgba(0, 0, 0, 0.5);
                border-top: 3px solid;
                border-image: linear-gradient(45deg, #ff00de, #00fff2) 1;
            }
            
            .play-btn {
                width: 60px;
                height: 60px;
                border-radius: 50%;
                border: 3px solid #00fff2;
                background: linear-gradient(135deg, #ff00de, #ff6b00);
                color: white;
                font-size: 1.5rem;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.5s;
                animation: extremePulse 4s infinite;
                flex-shrink: 0;
            }
            
            .play-btn:hover {
                transform: scale(1.15) rotate(10deg);
                animation: wiggle 1s infinite, rainbowGlow 3s infinite;
            }
            
            .play-btn.playing {
                background: linear-gradient(135deg, #00fff2, #00ff88);
                animation: crazySpinZoom 6s infinite, rainbowGlow 4s infinite;
            }
            
            .audio-progress {
                flex: 1;
                height: 10px;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                overflow: hidden;
                position: relative;
            }
            
            .audio-progress-bar {
                height: 100%;
                background: linear-gradient(90deg, #ff00de, #00fff2, #ff6b00);
                background-size: 200% 100%;
                width: 0%;
                transition: width 0.1s linear;
                animation: gradientShift 5s infinite;
            }
            
            .audio-time {
                color: #00fff2;
                font-size: 0.9rem;
                font-weight: bold;
                text-shadow: 0 0 10px rgba(0, 255, 242, 0.8);
                min-width: 45px;
                text-align: center;
            }
            
            @media (max-width: 768px) {
                body {
                    padding: 1rem 0.5rem;
                }
                
                h1 {
                    font-size: 2rem;
                    letter-spacing: 0.2rem;
                }
                
                .subtitle {
                    font-size: 1rem;
                    letter-spacing: 0.15rem;
                }
                
                .container {
                    padding: 1rem;
                }
                
                .search-form {
                    flex-direction: column;
                    gap: 1rem;
                }
                
                #searchInput, #searchBtn {
                    width: 100%;
                    font-size: 1rem;
                }
                
                #searchBtn {
                    padding: 1rem;
                }
                
                .results {
                    grid-template-columns: 1fr;
                    gap: 1.5rem;
                }
                
                .result-card {
                    padding: 1rem;
                }
                
                .result-title {
                    font-size: 1.2rem;
                }
                
                .result-artist {
                    font-size: 1rem;
                }
                
                .help-btn, .info-btn, .lang-btn {
                    width: 55px;
                    height: 55px;
                    font-size: 1.8rem;
                    border: 4px solid white;
                }
                
                .help-btn {
                    bottom: 20px;
                    left: 15px;
                }
                
                .info-btn {
                    bottom: 20px;
                    left: 85px;
                }
                
                .lang-btn {
                    bottom: 20px;
                    left: 155px;
                    font-size: 1.5rem;
                }
                
                .magic-button {
                    bottom: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    padding: 1rem 2rem;
                    font-size: 1rem;
                    letter-spacing: 0.1rem;
                }
                
                .help-content, .info-content {
                    margin: 1rem;
                    padding: 1.5rem;
                    max-width: 90%;
                    max-height: 85vh;
                }
                
                .help-content h2, .info-content h2 {
                    font-size: 1.5rem;
                }
                
                .info-content h3 {
                    font-size: 1.2rem;
                }
                
                .help-content p, .info-content p, .info-content li {
                    font-size: 0.95rem;
                }
                
                .search-container {
                    padding: 1.5rem;
                }
                
                .loading-text {
                    font-size: 1rem;
                }
                
                .error-content {
                    padding: 1.5rem;
                }
            }
            
            @media (max-width: 480px) {
                h1 {
                    font-size: 1.5rem;
                    letter-spacing: 0.1rem;
                }
                
                .subtitle {
                    font-size: 0.9rem;
                }
                
                .help-btn, .info-btn, .lang-btn {
                    width: 45px;
                    height: 45px;
                    font-size: 1.3rem;
                    border: 3px solid white;
                }
                
                .help-btn {
                    bottom: 15px;
                    left: 10px;
                }
                
                .info-btn {
                    bottom: 15px;
                    left: 65px;
                }
                
                .lang-btn {
                    bottom: 15px;
                    left: 120px;
                    font-size: 1.1rem;
                }
                
                .magic-button {
                    padding: 0.8rem 1.2rem;
                    font-size: 0.8rem;
                    bottom: 15px;
                    left: 50%;
                    transform: translateX(-50%);
                }
                
                .result-card img {
                    height: 200px;
                }
                
                .play-btn {
                    width: 50px;
                    height: 50px;
                    font-size: 1.2rem;
                }
                
                .audio-time {
                    font-size: 0.9rem;
                }
                
                .info-content {
                    padding: 1rem;
                }
                
                .ai-badge {
                    font-size: 0.9rem;
                    padding: 0.4rem 0.8rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="black-hole-overlay"></div>
        <div class="unicorn-overlay">🦄</div>
        <div class="rainbow-trail"></div>
        
        <button class="help-btn" onclick="toggleHelp()">?</button>
        <button class="info-btn" onclick="toggleInfo()">🤖</button>
        <button class="magic-button" onclick="triggerMagic()">🌀 MAGISCHE REISE 🦄</button>
        
        <div class="help-modal" id="helpModal">
            <div class="help-content" id="helpContent">
                <h2>🎵 Wie funktioniert's?</h2>
                <p><strong>Schritt 1:</strong> Gib den Namen eines Songs, Künstlers oder Albums in die Suchleiste ein.</p>
                <p><strong>Schritt 2:</strong> Klicke auf "SUCHEN" oder drücke Enter.</p>
                <p><strong>Schritt 3:</strong> Durchstöbere die Ergebnisse! Jede Karte zeigt:</p>
                <ul style="margin-left: 1.5rem; margin-bottom: 1rem;">
                    <li>🎵 Song-Titel</li>
                    <li>🎤 Künstlername</li>
                    <li>🖼️ Künstlerbild</li>
                    <li>▶️ Audio-Vorschau-Player (30 Sekunden)</li>
                </ul>
                <p><strong>Schritt 4:</strong> Klicke auf den Play-Button (▶️), um eine 30-Sekunden-Vorschau zu hören!</p>
                <p><strong>Tipps:</strong></p>
                <ul style="margin-left: 1.5rem; margin-bottom: 1rem;">
                    <li>Fahre mit der Maus über die Karten für verrückte Effekte!</li>
                    <li>Es kann immer nur eine Vorschau gleichzeitig abgespielt werden</li>
                    <li>Klicke auf Pause (⏸️), um die Wiedergabe zu stoppen</li>
                </ul>
                <button class="close-btn" onclick="toggleHelp()">Verstanden!</button>
            </div>
        </div>
        
        <div class="info-modal" id="infoModal">
            <div class="info-content">
                <h2>🤖 KI-Generierte Website 🎨</h2>
                
                <div class="ai-badge">
                    ✨ 100% KI-GENERIERT ✨
                </div>
                
                <p>Diese gesamte Website wurde vollständig durch Künstliche Intelligenz erstellt - vom Design über den Code bis hin zu den Animationen!</p>
                
                <h3>🎯 Über diese Seite</h3>
                <p>Diese Music App ist ein privates Hobby-Projekt, das die Möglichkeiten moderner KI-Technologie demonstriert. Die Anwendung nutzt die Deezer API, um Musiksuche und Vorschau-Funktionen bereitzustellen.</p>
                
                <h3>⚠️ Haftungsausschluss</h3>
                <div class="disclaimer-box">
                    <p><strong>Keine Gewährleistung:</strong> Diese Website wird "wie besehen" bereitgestellt. Es wird keine Garantie für die Richtigkeit, Vollständigkeit oder Aktualität der Inhalte übernommen.</p>
                    
                    <p><strong>Externe Links:</strong> Diese Seite nutzt die Deezer API. Für die Inhalte und Dienste von Deezer ist ausschließlich Deezer SA verantwortlich.</p>
                    
                    <p><strong>Keine Haftung:</strong> Der Betreiber übernimmt keine Haftung für Schäden, die durch die Nutzung dieser Website entstehen könnten.</p>
                    
                    <p><strong>Datenschutz:</strong> Diese Website erhebt keine personenbezogenen Daten. Suchanfragen werden direkt an die Deezer API weitergeleitet. Bitte beachten Sie die Datenschutzbestimmungen von Deezer.</p>
                    
                    <p><strong>Urheberrecht:</strong> Alle Musikinhalte, Vorschauen und Bilder sind Eigentum der jeweiligen Rechteinhaber und werden über die Deezer API bereitgestellt.</p>
                </div>
                
                <h3>🎵 Technologie</h3>
                <ul>
                    <li>🐍 Backend: FastAPI (Python)</li>
                    <li>🎨 Frontend: Vanilla JavaScript + CSS</li>
                    <li>🎼 Musik-API: Deezer</li>
                    <li>🤖 Erstellt mit: Claude AI</li>
                </ul>
                
                <p style="text-align: center; margin-top: 1.5rem; font-size: 0.9rem; opacity: 0.8;">
                    Dies ist ein nicht-kommerzielles Projekt ohne Gewinnabsicht.
                </p>
                
                <button class="close-btn" onclick="toggleInfo()">Verstanden!</button>
            </div>
        </div>
        
        <div class="container">
            <div class="header">
                <h1>🎵 CRAZY MUSIX EXPLORER 🎵</h1>
                <p class="subtitle">~ Entdecke Deinen nächsten Lieblingssong ~</p>
            </div>
            
            <div class="search-container">
                <form class="search-form" onsubmit="searchMusic(event)">
                    <input
                        type="text"
                        id="searchInput"
                        placeholder="Suche nach Songs, Künstlern, Alben..."
                        required
                    >
                    <button type="submit" id="searchBtn">🔍 SUCHEN</button>
                </form>
            </div>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <div class="loading-text">Durchsuche das Universum nach deiner Musik...</div>
            </div>
            
            <div class="error" id="error">
                <p class="error-text" id="errorText"></p>
            </div>
            
            <div class="results" id="results"></div>
        </div>
        
        <script>
            function toggleHelp() {
                const modal = document.getElementById('helpModal');
                modal.classList.toggle('active');
            }
            
            function toggleInfo() {
                const modal = document.getElementById('infoModal');
                modal.classList.toggle('active');
            }
            
            
            
            async function searchMusic(event) {
                event.preventDefault();
                
                const query = document.getElementById('searchInput').value.trim();
                const loading = document.getElementById('loading');
                const error = document.getElementById('error');
                const results = document.getElementById('results');
                
                // Reset UI
                loading.classList.add('active');
                error.classList.remove('active');
                results.innerHTML = '';
                
                try {
                    const response = await fetch('/api/search?q=' + encodeURIComponent(query));
                    
                    if (!response.ok) {
                        throw new Error('Search failed: ' + response.statusText);
                    }
                    
                    const data = await response.json();
                    
                    loading.classList.remove('active');
                    
                    if (!data.data || data.data.length === 0) {
                        showError('No results found. Try a different search term!');
                        return;
                    }
                    
                    displayResults(data.data);
                    
                } catch (err) {
                    loading.classList.remove('active');
                    showError('Oops! Something went wrong: ' + err.message);
                }
            }
            
            let currentAudio = null;
            let currentPlayBtn = null;
            
            function displayResults(tracks) {
                const results = document.getElementById('results');
                results.innerHTML = '';
                
                tracks.forEach((track, index) => {
                    const card = document.createElement('div');
                    card.className = 'result-card';
                    card.style.animationDelay = index * 0.1 + 's';
                    
                    const artistImage = track.artist.picture_big || track.artist.picture_medium || track.album.cover_big;
                    const previewUrl = track.preview;
                    
                    card.innerHTML = `
                        <img src="${artistImage}" alt="${track.artist.name}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22280%22 height=%22280%22%3E%3Crect fill=%22%23667eea%22 width=%22280%22 height=%22280%22/%3E%3Ctext fill=%22white%22 x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 font-size=%2240%22%3E🎵%3C/text%3E%3C/svg%3E'">
                        <div class="result-info">
                            <div class="result-title">${escapeHtml(track.title)}</div>
                            <div class="result-artist">${escapeHtml(track.artist.name)}</div>
                        </div>
                        ${previewUrl ? `
                        <div class="audio-controls">
                            <button class="play-btn" data-preview="${previewUrl}" data-index="${index}">
                                ▶️
                            </button>
                            <div class="audio-progress">
                                <div class="audio-progress-bar" id="progress-${index}"></div>
                            </div>
                            <div class="audio-time" id="time-${index}">0:00</div>
                        </div>
                        ` : '<div class="audio-controls"><div style="color: #ff6b6b; text-align: center; width: 100%;">No preview available</div></div>'}
                    `;
                    
                    results.appendChild(card);
                    
                    // Add event listener for play button
                    if (previewUrl) {
                        const playBtn = card.querySelector('.play-btn');
                        playBtn.addEventListener('click', (e) => {
                            e.stopPropagation();
                            toggleAudio(previewUrl, playBtn, index);
                        });
                    }
                });
            }
            
            function toggleAudio(previewUrl, playBtn, index) {
                // If clicking the same button, toggle play/pause
                if (currentAudio && currentPlayBtn === playBtn) {
                    if (currentAudio.paused) {
                        currentAudio.play();
                        playBtn.textContent = '⏸️';
                        playBtn.classList.add('playing');
                    } else {
                        currentAudio.pause();
                        playBtn.textContent = '▶️';
                        playBtn.classList.remove('playing');
                    }
                    return;
                }
                
                // Stop current audio if playing
                if (currentAudio) {
                    currentAudio.pause();
                    currentAudio.currentTime = 0;
                    if (currentPlayBtn) {
                        currentPlayBtn.textContent = '▶️';
                        currentPlayBtn.classList.remove('playing');
                    }
                }
                
                // Create and play new audio
                currentAudio = new Audio(previewUrl);
                currentPlayBtn = playBtn;
                
                currentAudio.play();
                playBtn.textContent = '⏸️';
                playBtn.classList.add('playing');
                
                // Update progress bar and time
                currentAudio.addEventListener('timeupdate', () => {
                    const progress = (currentAudio.currentTime / currentAudio.duration) * 100;
                    const progressBar = document.getElementById('progress-' + index);
                    const timeDisplay = document.getElementById('time-' + index);
                    
                    if (progressBar) {
                        progressBar.style.width = progress + '%';
                    }
                    
                    if (timeDisplay) {
                        const currentTime = Math.floor(currentAudio.currentTime);
                        const minutes = Math.floor(currentTime / 60);
                        const seconds = currentTime % 60;
                        timeDisplay.textContent = minutes + ':' + seconds.toString().padStart(2, '0');
                    }
                });
                
                // Reset when audio ends
                currentAudio.addEventListener('ended', () => {
                    playBtn.textContent = '▶️';
                    playBtn.classList.remove('playing');
                    const progressBar = document.getElementById('progress-' + index);
                    const timeDisplay = document.getElementById('time-' + index);
                    if (progressBar) progressBar.style.width = '0%';
                    if (timeDisplay) timeDisplay.textContent = '0:00';
                    currentAudio = null;
                    currentPlayBtn = null;
                });
                
                // Handle errors
                currentAudio.addEventListener('error', () => {
                    playBtn.textContent = '❌';
                    playBtn.classList.remove('playing');
                    playBtn.disabled = true;
                    showError('Failed to load audio preview');
                });
            }
            
            function showError(message) {
                const error = document.getElementById('error');
                const errorText = document.getElementById('errorText');
                errorText.textContent = message;
                error.classList.add('active');
            }
            
            function escapeHtml(text) {
                const div = document.createElement('div');
                div.textContent = text;
                return div.innerHTML;
            }
            
            // Close help modal when clicking outside
            document.getElementById('helpModal').addEventListener('click', function(e) {
                if (e.target === this) {
                    toggleHelp();
                }
            });
            
            // Close info modal when clicking outside
            document.getElementById('infoModal').addEventListener('click', function(e) {
                if (e.target === this) {
                    toggleInfo();
                }
            });
            
            function triggerMagic() {
                const body = document.body;
                
                // Phase 1: Black hole sucks everything in
                body.classList.add('black-hole-active');
                
                // Phase 2: After 2 seconds, remove black hole and add unicorn
                setTimeout(() => {
                    body.classList.remove('black-hole-active');
                    body.classList.add('unicorn-return');
                }, 2000);
                
                // Phase 3: After 4 seconds total, remove unicorn class
                setTimeout(() => {
                    body.classList.remove('unicorn-return');
                }, 4000);
            }
        </script>
    </body>
    </html>
    """
    return html_content


@app.get("/api/search")
async def search_music(q: str = Query(..., description="Search query for music (artist, track, album)")):
    """
    Search for music using the Deezer API.
    
    Args:
        q: Search query string (required)
    
    Returns:
        dict: JSON response from Deezer API containing search results
        
    Raises:
        HTTPException: If the Deezer API request fails
    """
    try:
        # Make request to Deezer API
        response = await http_client.get(
            "https://api.deezer.com/search",
            params={"q": q}
        )
        response.raise_for_status()
        
        # Return the JSON response from Deezer
        return response.json()
        
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Deezer API returned an error: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Failed to connect to Deezer API: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """
    Health check endpoint that returns the application status and current timestamp.
    
    Returns:
        dict: A dictionary containing status and timestamp in ISO 8601 format
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.on_event("shutdown")
async def shutdown_event():
    """
    Cleanup function to close the HTTP client when the application shuts down.
    """
    await http_client.aclose()