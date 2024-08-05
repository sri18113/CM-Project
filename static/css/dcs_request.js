const data = [
    { deviceName: 'Device 1', serialNumber: '123456', requestorId: '001', domain: 'Domain 1', clli: 'CLLI 1' },
    { deviceName: 'Device 2', serialNumber: '654321', requestorId: '002', domain: 'Domain 2', clli: 'CLLI 2' },
    { deviceName: 'Device 3', serialNumber: '111111', requestorId: '003', domain: 'Domain 3', clli: 'CLLI 3' },
    { deviceName: 'Device 4', serialNumber: '222222', requestorId: '004', domain: 'Domain 4', clli: 'CLLI 4' },
    { deviceName: 'Device 5', serialNumber: '333333', requestorId: '005', domain: 'Domain 5', clli: 'CLLI 5' },
    { deviceName: 'Device 6', serialNumber: '444444', requestorId: '006', domain: 'Domain 6', clli: 'CLLI 6' },
    { deviceName: 'Device 7', serialNumber: '555555', requestorId: '007', domain: 'Domain 7', clli: 'CLLI 7' },
    { deviceName: 'Device 8', serialNumber: '666666', requestorId: '008', domain: 'Domain 8', clli: 'CLLI 8' }
];

let currentPage = 1;
const rowsPerPage = 6;

function renderTable() {
    const tableBody = document.getElementById('table-body');
    tableBody.innerHTML = '';
    const start = (currentPage - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    const pageData = data.slice(start, end);
    pageData.forEach((row, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><input type="checkbox"></td>
            <td>${row.deviceName}
                <div class="device-actions">
                    <a href="#" onclick="openEditPage(${start + index})">Edit</a> |
                    <a href="#" onclick="cloneEntry(${start + index})">Clone</a>
                </div>
            </td>
            <td contenteditable="false">${row.serialNumber}</td>
            <td contenteditable="false">${row.requestorId}</td>
            <td contenteditable="false">${row.domain}</td>
            <td contenteditable="false">${row.clli}</td>
            <td class="action-icons">
                <span onclick="editEntry(this, ${start + index})">✏️</span>
                <span onclick="saveEntry(this, ${start + index})" style="display:none;">💾</span>
                <span onclick="deleteEntry(${start + index})">🗑️</span>
            </td>
        `;
        tableBody.appendChild(tr);
    });
    renderPagination();
}

function renderPagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';
    const totalPages = Math.ceil(data.length / rowsPerPage);
    for (let i = 1; i <= totalPages; i++) {
        const button = document.createElement('button');
        button.innerText = i;
        button.onclick = () => goToPage(i);
        if (i === currentPage) {
            button.style.backgroundColor = '#3498db';
        }
        pagination.appendChild(button);
    }
}

function goToPage(page) {
    currentPage = page;
    renderTable();
}

function openCreateModal() {
    document.getElementById('createModal').style.display = 'block';
}

function closeCreateModal() {
    document.getElementById('createModal').style.display = 'none';
}

function createNewEntry() {
    const newDeviceName = document.getElementById('newDeviceName').value;
    const newSerialNumber = document.getElementById('newSerialNumber').value;
    const newRequestorId = document.getElementById('newRequestorId').value;
    const newDomain = document.getElementById('newDomain').value;
    const newClli = document.getElementById('newClli').value;
    data.push({
        deviceName: newDeviceName,
        serialNumber: newSerialNumber,
        requestorId: newRequestorId,
        domain: newDomain,
        clli: newClli
    });
    closeCreateModal();
    renderTable();
}

function openEditPage(index) {
    const deviceName = data[index].deviceName;
    const newPage = window.open('', '_blank');
    newPage.document.write(`<h1>${deviceName}</h1>`);
}

function cloneEntry(index) {
    const clonedEntry = { ...data[index] };
    data.splice(index + 1, 0, clonedEntry);
    renderTable();
}

function deleteEntry(index) {
    data.splice(index, 1);
    renderTable();
}

function deleteSelectedRows() {
    const checkboxes = document.querySelectorAll('tbody input[type="checkbox"]:checked');
    checkboxes.forEach(checkbox => {
        const rowIndex = Array.from(checkbox.closest('tbody').children).indexOf(checkbox.closest('tr'));
        data.splice((currentPage - 1) * rowsPerPage + rowIndex, 1);
    });
    renderTable();
}

function selectAllRows(source) {
    const checkboxes = document.querySelectorAll('tbody input[type="checkbox"]');
    checkboxes.forEach(checkbox => checkbox.checked = source.checked);
}

function refreshTable() {
    renderTable();
}

function editEntry(element, index) {
    const row = element.closest('tr');
    const cells = row.querySelectorAll('td');
    cells.forEach(cell => {
        if (cell.hasAttribute('contenteditable')) {
            cell.setAttribute('contenteditable', 'true');
            cell.style.backgroundColor = '#f2f2f2';
        }
    });
    element.style.display = 'none';
    element.nextElementSibling.style.display = 'inline';
}

function saveEntry(element, index) {
    const row = element.closest('tr');
    const cells = row.querySelectorAll('td');
    data[index].serialNumber = cells[2].innerText;
    data[index].requestorId = cells[3].innerText;
    data[index].domain = cells[4].innerText;
    data[index].clli = cells[5].innerText;
    cells.forEach(cell => {
        if (cell.hasAttribute('contenteditable')) {
            cell.setAttribute('contenteditable', 'false');
            cell.style.backgroundColor = 'transparent';
        }
    });
    element.style.display = 'none';
    element.previousElementSibling.style.display = 'inline';
}

document.addEventListener('DOMContentLoaded', () => {
    renderTable();
});
