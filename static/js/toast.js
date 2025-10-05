function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-teal-50', 'border-teal-500', 'text-teal-600',
        'bg-white', 'border-stone-300', 'text-stone-800'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-teal-50', 'border-teal-500', 'text-teal-600');
        toastComponent.style.border = '1px solid #14b8a6';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-white', 'border-stone-300', 'text-stone-800');
        toastComponent.style.border = '1px solid #d6d3d1';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-10');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-10');
    }, duration);
}