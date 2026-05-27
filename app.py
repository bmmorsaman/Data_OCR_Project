import streamlit as st

# ครอบระบบทั้งหมดด้วย Try เพื่อดักจับอาการจอดำ
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from google import genai
    from google.genai import types
    import json
    from PIL import Image
    import io

    # ตั้งค่า (อย่าลืมเปลี่ยนเป็นของคุณ)
    GEMINI_API_KEY = "AIzaSyC0BkfCKLSsGS-yEZjnsETW4rlNjHFxSwQ"
    GOOGLE_SHEET_NAME = "Data_OCR_Project"

    st.title("📸 สแกนตารางกระดาษ เข้า Google Sheets")
    st.write("ถ้าเห็นข้อความนี้ แสดงว่าระบบหน้าเว็บปกติแล้วครับ!")

    # ปุ่มเปิดกล้อง/อัปโหลดไฟล์
    uploaded_file = st.camera_input("ถ่ายภาพตารางบนกระดาษ")
    if not uploaded_file:
        uploaded_file = st.file_uploader("หรือเลือกรูปภาพจากในเครื่อง", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="รูปภาพของคุณ", use_container_width=True)
        st.success("อัปโหลดรูปภาพสำเร็จ! พร้อมประมวลผล")

except Exception as e:
    # ถ้าโค้ดพังตรงไหน ให้พ่นออกมาบนหน้าเว็บ ไม่ต้องปล่อยให้จอดำ
    st.error("❌ พบข้อผิดพลาดในการรันแอปพลิเคชัน:")
    st.code(str(e))