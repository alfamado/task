# project/contact.py

# In-memory store: each contact = [name, phone, age (int), job]
contacts = []


# ---------- validators (internal) ----------
def _is_valid_name(name: str) -> bool:
    return isinstance(name, str) and name.replace(" ", "").replace("-", "").replace("'", "").isalpha()

def _is_valid_job(job: str) -> bool:
    return isinstance(job, str) and job.replace(" ", "").replace("-", "").replace("'", "").isalpha()

def _is_valid_phone(phone: str) -> bool:
    return isinstance(phone, str) and phone.isdigit() and len(phone) == 11 and phone.startswith("0")
def _is_valid_age(age: str) -> bool:
    return age.isdigit() and 0 < int(age) < 120


def _coerce_age(age):
    """Accept str/int. Return (ok, value_or_msg)."""
    if isinstance(age, int):
        return True, age
    if isinstance(age, str) and age.isdigit():
        return True, int(age)
    return False, "Age must be digits only."

def _phone_exists(phone: str, ignore_index: int = None) -> bool:
    for i, c in enumerate(contacts):
        if c[1] == phone and i != ignore_index:
            return True
    return False


# ---------- CRUD API ----------
def create(name: str, phone: str, age, job: str):
    """Return (ok, msg). On success, contact is appended."""
    if not _is_valid_name(name or ""):
        return False, "Invalid name. Use alphabets only."
    if not _is_valid_phone(phone or ""):
        return False, "Invalid phone. Must be 11 digits, start with 0."
    if _phone_exists(phone):
        return False, "Phone already exists."
    ok, age_val = _coerce_age(age)
    if not ok:
        return False, age_val # error message
    if not _is_valid_job(job or ""):
        return False, "Invalid job title. Use alphabets only."

    contacts.append([name.strip(), phone.strip(), age_val, job.strip()])
    return True, "Contact created."


def read():
    """Return the list object (caller should not mutate recklessly)."""
    return contacts


def update(index: int, field, new_value):
    """
    field can be 0/1/2/3 or 'name'/'phone'/'age'/'job'.
    Returns (ok, msg).
    """
    if not (0 <= index < len(contacts)):
        return False, "Invalid contact index."

    field_map = {0: "name", 1: "phone", 2: "age", 3: "job"}
    if isinstance(field, int):
        field = field_map.get(field)
    if field not in ("name", "phone", "age", "job"):
        return False, "Invalid field. Use 0-3 or name/phone/age/job."

    if field == "name":
        if not _is_valid_name(new_value or ""):
            return False, "Invalid name. Use alphabets only."
        contacts[index][0] = new_value.strip()

    elif field == "phone":
        if not _is_valid_phone(new_value or ""):
            return False, "Invalid phone. Must be 11 digits, start with 0."
        if _phone_exists(new_value, ignore_index=index):
            return False, "Phone already exists."
        contacts[index][1] = new_value.strip()

    elif field == "age":
        ok, age_val = _coerce_age(new_value)
        if not ok:
            return False, age_val
        contacts[index][2] = age_val

    elif field == "job":
        if not _is_valid_job(new_value or ""):
            return False, "Invalid job title. Use alphabets only."
        contacts[index][3] = new_value.strip()

    return True, "Contact updated."


def delete(index: int):
    """Return (ok, msg)."""
    if not (0 <= index < len(contacts)):
        return False, "Invalid contact index."
    contacts.pop(index)
    return True, "Contact deleted."


def search(keyword: str):
    """
    Case-insensitive name contains OR exact phone match.
    Returns list of (1-based_index, contact_list).
    """
    if not keyword:
        return []
    kw = keyword.strip()
    results = []
    for i, c in enumerate(contacts, start=1):
        if kw.lower() in c[0].lower() or kw == c[1]:
            results.append((i, c))
    return results