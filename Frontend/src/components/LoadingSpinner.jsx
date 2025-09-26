const LoadingSpinner = () => {
  return (
    <div
      className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"
      role="status"
      aria-label="Loading"
    >
      <span className="sr-only">Loading...</span>
    </div>
  );
};

export default LoadingSpinner;