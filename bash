docker build -t retinascan-backend .
npm install react-qr-code
git init
git add .
git commit -m "Initial backend commit"
git remote add origin https://github.com/yourusername/retinascan-backend.git
git push -u origin main
curl -X POST https://retinascan-backend.up.railway.app/analyze \
  -F "image=@sample.jpg"
pip install torch==2.8.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
curl -X POST https://retinascan-pro.onrender.com/analyze \
  -F "image=@sample.jpg"
https://retinascan-prot.onrender.com/health
curl -X POST https://retinascan-prot.onrender.com/analyze \
  -F "image=@sample.jpg"


