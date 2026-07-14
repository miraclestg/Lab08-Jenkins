from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lab 08 - Flask</title>
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            body{
                min-height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background:linear-gradient(
                    135deg,
                    #f3e8ff,
                    #e9d5ff,
                    #ddd6fe
                );
            }

            .card{
                width:500px;
                background:rgba(255,255,255,0.9);
                backdrop-filter:blur(10px);
                border-radius:25px;
                padding:40px;
                text-align:center;
                box-shadow:0 15px 35px rgba(128,90,213,0.2);
                transition:0.3s;
            }

            .card:hover{
                transform:translateY(-5px);
            }

            .icon{
                font-size:60px;
                margin-bottom:15px;
            }

            h1{
                color:#6b21a8;
                margin-bottom:10px;
            }

            h2{
                color:#8b5cf6;
                font-weight:500;
                margin-bottom:25px;
            }

            .info{
                text-align:left;
                margin-top:20px;
            }

            .info-item{
                background:#f5f3ff;
                margin:12px 0;
                padding:15px;
                border-radius:15px;
                border-left:5px solid #a855f7;
            }
	    .social-links{
    display:flex;
    justify-content:center;
    gap:15px;
    margin-top:25px;
    flex-wrap:wrap;
}

.social-btn{
    display:flex;
    align-items:center;
    gap:10px;
    text-decoration:none;
    color:white;
    padding:12px 24px;
    border-radius:50px;
    font-weight:600;
    transition:all 0.3s ease;
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
}

.social-btn i{
    width:30px;
    height:30px;
    border-radius:50%;
    background:rgba(255,255,255,0.2);
    display:flex;
    align-items:center;
    justify-content:center;
}

.social-btn:hover{
    transform:translateY(-4px);
}

.facebook{
    background:#1877f2;
}

.github{
    background:#24292e;
}

.email{
    background:#9333ea;
}

            .label{
                font-weight:bold;
                color:#6b21a8;
            }

            .footer{
                margin-top:25px;
                color:#7c3aed;
                font-size:14px;
            }

            .badge{
                display:inline-block;
                margin-top:15px;
                background:#c084fc;
                color:white;
                padding:8px 18px;
                border-radius:50px;
                font-weight:bold;
            }
        </style>
    </head>
    <body>

        <div class="card">
            

            <h1>BÀI THỰC HÀNH LAB 03</h1>
            <h2>TRIỂN KHAI CI/CD PIPELINE VỚI JENKINS VÀ DOCKER</h2>

            <div class="badge">Python Flask</div>

            <div class="info">
                <div class="info-item">
                    <span class="label">Họ và tên:</span>
                    Lý Hồng Phương Ân
                </div>

                <div class="info-item">
                    <span class="label">MSSV:</span>
                    23DH110170
                </div>

                <div class="info-item">
                    <span class="label">Môn học:</span>
                    Cloud Computing
                </div>

                <div class="social-links">

    <a class="social-btn facebook"
       href="https://www.facebook.com/ly.hong.phuong.an.2024/"
       target="_blank">
        <i class="fab fa-facebook-f"></i>
        Facebook
    </a>

    <a class="social-btn github"
       href="https://github.com/"
       target="_blank">
        <i class="fab fa-github"></i>
        GitHub
    </a>

    <a class="social-btn email"
       href="mailto:lyhongphuongan@gmail.com">
        <i class="fas fa-envelope"></i>
        Email
    </a>

</div>

            <div class="footer">
                © 2026 - Lab 08 CI/CD PIPELINE
            </div>
        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)