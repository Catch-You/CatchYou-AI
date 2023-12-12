# tmux <br/>
세션 생성 - tmux new -s 'session name' <br/>
세션 확인 - tmux ls <br/>
세션 불러오기 - tmux attach -t 'session name' <br/>
세션 나가기 - ctrl + b + d<br/> 

# FastAPI <br/>
실행 - uvicorn main:app —reload —host=0.0.0.0 —port 8080 <br/>
주소 - http://43.203.10.182:8080/docs/<br/>
POST /api/generate_and_save로 요청하면 S3 Bucket에 저장된 이미지 URL을 return 받으실 수 있습니다.
