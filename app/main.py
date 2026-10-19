"""Minimal DevOps student HTTP application (Python standard library only)."""
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def student_info():
    return {
        "Name": os.getenv("STUDENT_NAME", "Nurdos"),
        "Surname": os.getenv("STUDENT_SURNAME", "Kanatbek"),
        "Group": os.getenv("STUDENT_GROUP", "IT2-2310"),
        "Student ID": os.getenv("STUDENT_ID", "37253"),
    }


def render_student_info():
    return "\n".join(f"{label}: {value}" for label, value in student_info().items())


class StudentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status, text = 200, "OK\n"
        elif self.path in ("/", "/student"):
            status = 200
            text = ("DevOps Student Application\n"
                    "==========================\n"
                    f"{render_student_info()}\n"
                    "Application is running successfully!\n")
        else:
            status, text = 404, "Not found\n"
        content = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print("================================", flush=True)
    print("DevOps Student Application", flush=True)
    print("================================", flush=True)
    print(render_student_info(), flush=True)
    print("Application is running successfully!", flush=True)
    print(f"Listening on port {port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), StudentHandler).serve_forever()
