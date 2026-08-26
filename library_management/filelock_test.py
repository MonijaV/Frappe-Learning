import frappe
import time
from frappe.utils.synchronization import filelock


def test_filelock():
    file_path = frappe.get_site_path("private", "files", "lock_test.txt")
    with filelock("library_lock"):
        print("LOCK ACQUIRED")
        with open(file_path, "a") as f:
            f.write(f"Process started at {frappe.utils.now()}\n")
            print("Writing to file...")
            time.sleep(10)
            f.write(f"Process finished at {frappe.utils.now()}\n")
        print("LOCK RELEASED")