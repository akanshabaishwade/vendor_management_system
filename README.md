
# **Vendor Management System API Documentation**

## **Vendor Profile Management**

### **Create a new vendor**

- **URL:** `/api/vendors/`
- **Method:** `POST`
- **Description:** Create a new vendor profile.
- ![image](https://github.com/akanshabaishwade/vendor_management_system/assets/85228361/82a89147-adb9-4fdc-9f5c-907b282ac9a4)

- **Request Body:**
  ```json
  {
    "name": "Vendor Name",
    "contact_details": "Contact Details",
    "address": "Vendor Address",
    "vendor_code": "Unique Vendor Code"
  }
  ```


### List all vendors

- **URL:** `/api/vendors/`
- **Method:** `GET`
- **Description:** Retrieve a list of all vendors.

### Retrieve a specific vendor's details

- **URL:** `/api/vendors/{vendor_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific vendor.
- ![image](https://github.com/akanshabaishwade/vendor_management_system/assets/85228361/ab5ac903-be6e-40b4-bde7-9eebece41e06)
  

### Update a vendor's details

- **URL:** `/api/vendors/{vendor_id}/`
- **Method:** `PUT`
- **Description:** Update a vendor's details.
- ![image](https://github.com/akanshabaishwade/vendor_management_system/assets/85228361/2c3bd002-7455-4138-b8f6-da8e1861d340)

- **Request Body:**
  ```json
  {
    "name": "Updated Vendor Name",
    "contact_details": "Updated Contact Details",
    "address": "Updated Vendor Address",
    "vendor_code": "Updated Vendor Code"
  }
  ```

### Delete a vendor

- **URL:** `/api/vendors/{vendor_id}/`
- **Method:** `DELETE`
- **Description:** Delete a vendor.

## Purchase Order Tracking

### Create a purchase order

- **URL:** `/api/purchase_orders/`
- **Method:** `POST`
- **Description:** Create a new purchase order.
- **Request Body:**
  ```json
  {
    "po_number": "Purchase Order Number",
    "vendor": "Vendor ID",
    "order_date": "Order Date",
    "delivery_date": "Delivery Date",
    "items": "Items Details",
    "quantity": "Order Quantity",
    "status": "Order Status"
  }
  ```

### List all purchase orders

- **URL:** `/api/purchase_orders/`
- **Method:** `GET`
- **Description:** Retrieve a list of all purchase orders.

### Retrieve details of a specific purchase order

- **URL:** `/api/purchase_orders/{po_id}/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific purchase order.

### Update a purchase order

- **URL:** `/api/purchase_orders/{po_id}/`
- **Method:** `PUT`
- **Description:** Update a purchase order.
- **Request Body:**
  ```json
  {
    "po_number": "Updated Purchase Order Number",
    "vendor": "Updated Vendor ID",
    "order_date": "Updated Order Date",
    "delivery_date": "Updated Delivery Date",
    "items": "Updated Items Details",
    "quantity": "Updated Order Quantity",
    "status": "Updated Order Status"
  }
  ```

### Delete a purchase order

- **URL:** `/api/purchase_orders/{po_id}/`
- **Method:** `DELETE`
- **Description:** Delete a purchase order.

## Vendor Performance Evaluation

### Retrieve a vendor's performance metrics

- **URL:** `/api/vendors/{vendor_id}/performance`
- **Method:** `GET`
- **Description:** Retrieve performance metrics for a specific vendor.
- ![image](https://github.com/akanshabaishwade/vendor_management_system/assets/85228361/99f6870c-b9df-44a2-895a-33d205c372cf)


