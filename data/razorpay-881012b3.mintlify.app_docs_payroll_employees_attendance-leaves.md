> ## Documentation Index
> Fetch the complete documentation index at: https://razorpay-881012b3.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Attendance & Leaves

> Use the RazorpayX Payroll Dashboard as an employee to check attendance and apply for leaves.

<div style={{display:"flex",flexWrap:"wrap",alignItems:"center",gap:"0.35rem 0.9rem",border:"1px solid rgba(128,128,128,0.28)",borderRadius:"0.5rem",padding:"0.45rem 0.75rem",margin:"0 0 1.25rem",fontSize:"0.875rem"}}>
  <span style={{fontWeight:600}}>Available in</span>
  <span>🇮🇳 India</span>
</div>

Leaves and attendance form a critical part of every employee's payslip and personal management. On the Payroll Dashboard, you can:

* [Mark attendance](#mark-attendance)
  * [Update/Edit attendance for a past date](#edit-attendance)
  * [Delete incorrect attendance information](#delete-attendance)
* [Apply for leaves](#apply-for-leaves)
  * [Apply for leaves in bulk](#apply-leaves-in-bulk)
  * [View Leaves Status](#leave-status-indicator)
  * [View leave balance](#view-leave-balance)
* [Delete Leave & Attendance modification requests](#delete-requests)

Once you apply for leaves, they are sent to your managers for approval as configured under **Profile** → **Basic Information**. Both administrators and your manager can approve leave requests.

<Check>
  **Available Now!**

  Watch the video on to how to [mark attendance](/docs/payroll/video-tutorials#mark-and-modify-attendance) and [apply for leaves](/docs/payroll/video-tutorials#apply-for-leaves).
</Check>

<Info>
  **Handy Tips**

  * If your organisation has integrated [Payroll with Slack](/docs/payroll/integrations/slack), you can update your leaves and attendance from within the Slack App. Refer to the [leave commands](/docs/payroll/integrations/slack#how-it-works).
  * You can check in and check out of your organisation via the biometric device, if your organisation has enabled it.
</Info>

## Mark Attendance

To mark attendance:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Navigate to **Attendance** in the left menu.
3. Use the **CHECK IN** and **CHECK OUT** options on the **Leave & Attendance** page to mark attendance for the day. You can also edit it on a future date and send it for approval.
   <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-mark-attendance1.jpg" alt="Check in and check out for attendance RazorpayX Payroll" width="800" />

You have successfully marked your attendance for a single day.

<Warning>
  **Watch Out!**

  Ensure you allow Payroll to access your device's location. Click **Allow** in the pop-up modal during check in and check out.
</Warning>

#### Manage Attendance

You can edit and delete incorrect attendance data on the Payroll Dashboard. After you make changes to your attendance, we send your request to your manager for approval.

<AccordionGroup>
  <Accordion title="Edit Attendance">
    You can edit attendance for a past date to update your attendance information.

    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Go to to **Attendance** in the left menu → [**Attendance** table](#attendance-table).
    3. Navigate to the specific date for which you want to edit attendace. Click the edit icon in the **Edit** column against that date.
    4. In the **Change Attendance** pop-up window, update you attendance/leave information.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-leave-apply.jpg" alt="Apply leave on RazorpayX Payroll Dashboard" width="800" />

    This successfully raises the edit attendance request to the admin/manager for approval.
  </Accordion>

  <Accordion title="Delete Attendance">
    You can delete attendance for a specific date if you have added and saved your attendance for the incorrect date.

    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Go to **Attendance** in the left menu.
    3. Navigate to the specific date for which you want to delete your attendace. Click the edit icon in the **Edit** column against that date.
    4. In the **Change Attendance** pop-up window, click **DELETE ATTENDANCE**.
           <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-leave-apply.jpg" alt="Apply leave on RazorpayX Payroll Dashboard" width="800" />

    This successfully raises the delete attendance request to your admin/manager for approval.
  </Accordion>

  <Accordion title="View Attendance">
    After you mark your attendance for the day, we update the **Attendance** table. To view the attendance information for a specific date, navigate to the specific date in the table.

    Here you can view the **Date**, **Status**, **Check In** and **Check Out** times. We automatically update the **Duration** and add the **Remarks** provided by you or your manager in the specific columns.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-attendance-apply.jpg" alt="RazorpayX Payroll apply for leave" width="800" />
  </Accordion>
</AccordionGroup>

## Apply for Leaves

To apply for a leave:

1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
2. Go to **Attendance** in the left menu.
3. In the [**Attendance** table](#attendance-table), find the date on which you are on leave. Click the edit icon in the **Edit** column.

   <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-attendance-apply.jpg" alt="RazorpayX Payroll apply for leave" width="800" />
4. In the **Change Attendance** pop-up modal:
   1. Select the **Status**. Select the leave to avail from the drop-down menu.
   2. Leave the **Check In** and **Check Out** times blank.
   3. Enter **Remarks** as applicable.
   4. Click **SEND REQUEST**.

<img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-leave-apply.jpg" alt="Apply leave on RazorpayX Payroll Dashboard" width="800" />

This successfully creates a leave request for the chosen date. We update your attendance calendar after your manager/HR's approval.

#### Manage Leaves

You can edit and update, or delete your leave and leaves modification requests on the Payroll Dashboard.

<AccordionGroup>
  <Accordion title="Apply Leaves in Bulk">
    To apply for leaves in bulk:

    1. Log in to the [Payroll Dashboard](https://payroll.razorpay.com/dashboard).
    2. Go to **Attendance** in the left menu → [**Attendance** table](#attendance-table).
    3. Click **here** under the **Attendance** heading.

       This opens the **Apply for Leave** pop-up modal.
    4. Select the **From Date** and **To Date** in the modal.
    5. Click **SEND REQUEST**.

    <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-bulk-leave.jpg" alt="Update bulk leaves on Razorpay Payroll" width="800" />
  </Accordion>

  <Accordion title="Leave Status Indicator">
    Payroll indicates attendance/leaves using the following colours:

    | Colour | Description                                    |
    | ------ | ---------------------------------------------- |
    | Green  | Indicates `Present` days.                      |
    | Red    | Indicates `Approved`leave days.                |
    | Brown  | Indicates `Pending Approval` from the Manager. |

    <img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-leave-codes.jpg" alt="Razorpay Payroll leave status indicators" width="800" />
  </Accordion>

  <Accordion title="View Leave Balance">
    To view leave balance, click **VIEW LEAVES TAKEN** in the right pane. You can view the leaves taken and available balance in the **Leaves Taken** pop-up modal.
  </Accordion>
</AccordionGroup>

## Delete Requests

When you modify your attendance or add a leave, we raise the leave as a request with your manager. You can also choose to delete the request before your manager's approval.

1. Go to the **Open Requests** section on the **Leave & Attendance** page.
2. Select the check box against the list requests you have raised to delete them.

<img src="https://razorpay.com/docs/build/browser/assets/images/payroll-employees-leave-request.jpg" alt="Modify leave request. Select the check box to update on Razorpay Payroll" width="800" />

### Related Information

* [Employee Dashboard](/docs/payroll/employees)
* [Slack Integration](/docs/payroll/integrations/slack)
* [IT Declarations](/docs/payroll/employees/declarations)
