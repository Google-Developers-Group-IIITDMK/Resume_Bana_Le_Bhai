const Header = () => {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center py-4">
          <div className="flex items-center">
            <h1 className="text-2xl font-bold text-indigo-600">
              Resume Builder
            </h1>
          </div>
          <div className="text-sm text-gray-500">
            Build professional resumes in minutes
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;