def ReadNOS(data=None, location=None, authorization=None, buffer_size=16, return_type="NOSREAD_RECORD",
            sample_perc=1.0, stored_as="TEXTFILE", full_scan=False, manifest=False, row_format=None, header=True,
            **generic_arguments):
    """
    DESCRIPTION:
        ReadNOS() function enables access to external files in JSON, CSV, or Parquet format.
        You must have the EXECUTE FUNCTION privilege on TD_SYSFNLIB.READ_NOS.


    PARAMETERS:
        data:
            Optional Argument.
            Specifies the input teradataml DataFrame.
            Types: teradataml DataFrame

        location:
            Optional Argument.
            Specifies the location value, which is a Uniform Resource Identifier
            (URI) pointing to the data in the external object storage system. The
            location value includes the following components:
            Amazon S3:
                /connector/bucket.endpoint/[key_prefix].
            Azure Blob storage and Azure Data Lake Storage Gen2:
                /connector/container.endpoint/[key_prefix].
            Google Cloud Storage:
                /connector/endpoint/bucket/[key_prefix].

            connector:
                Identifies the type of external storage system where the data is located.
                Teradata requires the storage location to start with the following for
                all external storage locations:
                    * Amazon S3 storage location must begin with /S3 or /s3
                    * Azure Blob storage location (including Azure Data Lake Storage Gen2
                      in Blob Interop Mode) must begin with /AZ or /az.
                    * Google Cloud Storage location must begin with /GS or /gs.

            storage-account:
                Used by Azure. The Azure storage account contains your
                Azure storage data objects.

            endpoint:
                A URL that identifies the system-specific entry point for
                the external object storage system.

            bucket (Amazon S3, Google Cloud Storage) or container (Azure Blob
            storage and Azure Data Lake Storage Gen2):
                A container that logically groups stored objects in the
                external storage system.

            key_prefix:
                Identifies one or more objects in the logical organization of
                the bucket data. Because it is a key prefix, not an actual
                directory path, the key prefix may match one or more objects
                in the external storage. For example, the key prefix
                "/fabrics/cotton/colors/b/" would match objects
                /fabrics/cotton/colors/blue, /fabrics/cotton/colors/brown, and
                /fabrics/cotton/colors/black. If there are organization levels below
                those, such as /fabrics/cotton/colors/blue/shirts, the same key
                prefix would gather those objects too.
                Note:
                    Vantage validates only the first file it encounters from the
                    location key prefix.

            For example, this location value might specify all objects on an
            Amazon cloud storage system for the month of December, 2001:
            location = "/S3/YOUR-BUCKET.s3.amazonaws.com/csv/US-Crimes/csv-files/2001/Dec/"
                connector: S3
                bucket: YOUR-BUCKET
                endpoint: s3.amazonaws.com
                key_prefix: csv/US-Crimes/csv-files/2001/Dec/

            Following location could specify an individual storage object (or file), Day1.csv:
            location = "/S3/YOUR-BUCKET.s3.amazonaws.com/csv/US-Crimes/csv-files/2001/Dec/Day1.csv"
                connector: S3
                bucket: YOUR-BUCKET
                endpoint: s3.amazonaws.com
                key_prefix: csv/US-Crimes/csv-files/2001/Dec/Day1.csv

            Following location specifies an entire container in an Azure external
            object store (Azure Blob storage or Azure Data Lake Storage Gen2).
            The container may contain multiple file objects:
            location = "/AZ/YOUR-STORAGE-ACCOUNT.blob.core.windows.net/nos-csv-data"
                connector: AZ
                bucket: YOUR-STORAGE-ACCOUNT
                endpoint: blob.core.windows.net
                key_prefix: nos-csv-data

            This is an example of a Google Cloud Storage location:
            location = "/gs/storage.googleapis.com/YOUR-BUCKET/CSVDATA/RIVERS/rivers.csv"
                connector: GS
                bucket: YOUR-BUCKET
                endpoint: storage.googleapis.com,
                key_prefix: CSVDATA/RIVERS/rivers.csv
            Types: str

        authorization:
            Optional Argument.
            Specifies the authorization for accessing external storage. On any
            platform, you can specify an authorization object
            ([DatabaseName.]AuthorizationObjectName). You must have the EXECUTE
            privilege on AuthorizationObjectName. On Amazon S3 and Azure Blob
            storage and Azure Data Lake Storage Gen2, you can specify either an
            authorization object or a string in JSON format. The string specifies
            the USER (identification) and PASSWORD (secret_key) for accessing
            external storage. The following table shows the supported credentials
            for USER and PASSWORD (used in the CREATE AUTHORIZATION command):

            +-----------------------+--------------------------+--------------------------+
            |     System/Scheme     |           USER           |         PASSWORD         |
            +-----------------------+--------------------------+--------------------------+
            |          AWS          |      Access Key ID       |    Access Key Secret     |
            |                       |                          |                          |
            |   Azure / Shared Key  |   Storage Account Name   |   Storage Account Key    |
            |                       |                          |                          |
            |  Azure Shared Access  |   Storage Account Name   |    Account SAS Token     |
            |    Signature (SAS)    |                          |                          |
            |                       |                          |                          |
            |      Google Cloud     |      Access Key ID       |    Access Key Secret     |
            |   (S3 interop mode)   |                          |                          |
            |                       |                          |                          |
            | Google Cloud (native) |       Client Email       |       Private Key        |
            |                       |                          |                          |
            |  Public access object |      <empty string>      |      <empty string>      |
            |        stores         | Enclose the empty string | Enclose the empty string |
            |                       |    in single straight    |    in single straight    |
            |                       |      quotes: USER ''     |    quotes: PASSWORD ''   |
            +-----------------------+--------------------------+--------------------------+
                                        
            If you use a function mapping to define a wrapper for READ_NOS SQLE Engine
            function, you can specify the authorization in the function mapping.
            Note that [ INVOKER | DEFINER ] TRUSTED must be used with function mapping.
            To set the function mapping for ReadNOS() function, set the following
            configuration options with function mapping name.
                teradataml.options.configure.read_nos_function_mapping = "<function mapping name>"
            If you are using AWS IAM credentials, you can omit the AUTHORIZATION
            clause. When accessing GCS, Advanced SQL Engine uses either the
            S3-compatible connector or the native Google connector, depending on
            the user credentials.
            Types: str

        buffer_size:
            Optional Argument.
            Specifies the size of the network buffer to allocate when retrieving
            data from the external storage repository. 16 MB, which is the maximum
            value.
            Default Value: 16
            Types: int

        return_type:
            Optional Argument.
            Specifies the format in which data is returned.
            Permitted Values:
                * NOSREAD_RECORD:
                    Returns one row for each external record along with its metadata.
                    Access external records by specifying one of the following:
                        - Input teradataml DataFrame and location and teradataml DataFrame
                          on an empty table. For CSV, you can include a schema definition.
                        - Input teradataml DataFrame with a row for each external file. For
                          CSV, this method does not support a schema definition.

                    For an empty single-column input table, do the following:
                        - Define an input teradataml DataFrame with a single column, Payload,
                          with the appropriate data type:
                            JSON and CSV
                          This column determines the output Payload column return type.
                        - For location, specify the filepath.

                    For a multiple-column input table, define an input teradataml
                    DataFrame with the following columns:
                        - Location VARCHAR(2048) CHARACTER SET UNICODE
                        - ObjectVersionID VARCHAR(1024) CHARACTER SET UNICODE
                        - ObjectVersionID VARCHAR(1024) CHARACTER SET UNICODE
                        - OffsetIntoObject BIGINT
                        - ObjectLength BIGINT
                        - Payload JSON or VARCHAR for CSV
                    This teradataml DataFrame can be populated using the output of the
                    'NOSREAD_KEYS' return type.

                * NOSREAD_KEYS:
                    Retrieve the list of files from the path specified in the "location" argument.
                    A schema definition is not necessary.
                    'NOSREAD_KEYS' returns Location, ObjectVersionID, ObjectTimeStamp,
                    and ObjectLength (size of external file).

                * NOSREAD_PARQUET_SCHEMA:
                    Returns information about the Parquet data schema. If you are using
                    the "full_scan" option, use 'NOSREAD_PARQUET_SCHEMA'; otherwise you can use
                    'NOSREAD_SCHEMA' to get information about the Parquet schema. For information
                    about the mapping between Parquet data types and Teradata data types, see
                    Parquet External Files in Teradata Vantage™ - SQL Data Definition Language
                    Syntax and Examples, B035-1144.

                * NOSREAD_SCHEMA:
                     Returns the name and data type of each column of the file specified in
                     "location". Schema format can be JSON, CSV, or Parquet.
            Default Value: "NOSREAD_RECORD"
            Types: str

        sample_perc:
            Optional Argument.
            Specifies the percentage of rows to retrieve from the external
            storage repository when return_type is 'NOSREAD_RECORD'. The valid
            range of values is from 0.0 to 1.0, where 1.0 represents 100%
            of the rows.
            Default Value: 1.0
            Types: float

        stored_as:
            Optional Argument.
            Specifies the formatting style of the external data.
            Permitted Values:
                * PARQUET-
                    The external data is formatted as Parquet. This is a
                    required parameter for Parquet data.
                * TEXTFILE-
                    The external data uses a text-based format, such as
                    CSV or JSON.
            Default Value: "TEXTFILE"
            Types: str

        full_scan:
            Optional Argument.
            Specifies whether ReadNOS() function scans columns of variable length
            types (CHAR, VARCHAR, BYTE, VARBYTE, JSON, and BSON) to discover the
            maximum length.
            When set to True, the size of variable length data is determined
            from the Parquet data.
            Note:
                Choosing this value can impact performance because all variable length
                data type columns in each Parquet file at the location must be scanned
                to assess the value having the greatest length.
            When set to False, variable length field sizes are assigned the
            Vantage maximum value for the particular data type.
            Note:
                "full_scan" is only used with a "return_type" of 'NOSREAD_PARQUET_SCHEMA'.
            Default Value: False
            Types: bool

        manifest:
            Optional Argument.
            Specifies whether the location value points to a manifest file (a
            file containing a list of files to read) or object name. The object
            name can include the full path or a partial path. It must identify a
            single file containing the manifest.
            Note:
                The individual entries within the manifest file must show
                complete paths.
            Below is an example of a manifest file that contains a list of entries
            to locations in JSON format.
            {
              "entries": [
                    {"url":"s3://nos-core-us-east-1/UNICODE/JSON/mln-key/data-10/data-8_9_02-10.json"},
                    {"url":"s3://nos-core-us-east-1/UNICODE/JSON/mln-key/data-10/data-8_9_02-101.json"},
                    {"url":"s3://nos-core-us-east-1/UNICODE/JSON/mln-key/data-10/data-10-01/data-8_9_02-102.json"},
                    {"url":"s3://nos-core-us-east-1/UNICODE/JSON/mln-key/data-10/data-10-01/data-8_9_02-103.json"}
               ]
            }
            Default Value: False
            Types: bool

        row_format:
            Optional Argument.
            Specifies the encoding format of the external row.
            For example:
                row_format = json.dumps({"field_delimiter":",", "record_delimiter":"\\n", "character_set":"LATIN"}).

            Specify "row_format" using JSON format. It can include only the three
            keys shown above. Key names and values are case-specific, except for
            the value for "character_set", which can use any combination of
            letter cases.
            The row format character set specification must be compatible with
            character set of the Payload column.
            Do not specify "row_format" for Parquet format data.
            For a JSON column, these are the default values:
                UNICODE:
                    row_format = json.dumps({"record_delimiter":"\\n", "character_set":"UTF8"})
                LATIN:
                    row_format = json.dumps({"record_delimiter":"\\n", "character_set":"LATIN"})
            For a CSV column, these are the default values:
                UNICODE:
                    row_format = '{"character_set":"UTF8"}'
                    This is the default if you do not specify an input data
                    for ReadNOS() function.
                LATIN:
                    row_format = '{"character_set":"LATIN"}'
            You can specify the following options:
                field_delimiter: The default is "," (comma). You can also specify a
                                 custom field delimiter, such as tab "\\t".
                record_delimiter: New line feed character: "\\n". A line feed
                                  is the only acceptable record delimiter.
                character_set: "UTF8" or "LATIN". If you do not specify a "row_format"
                               or payload column, Vantage assumes UTF8 Unicode.
            Types: str

        header:
            Optional Argument.
            Specifies whether the first row of data in an input CSV file is
            interpreted as column headings for the subsequent rows of data. Use
            this parameter only when a CSV input file is not associated with a
            separate schema object that defines columns for the CSV data.
            Default Value: True
            Types: bool

        **generic_arguments:
            Specifies the generic keyword arguments SQLE functions accept.
            Below are the generic keyword arguments:
                persist:
                    Optional Argument.
                    Specifies whether to persist the results of the function in table or not.
                    When set to True, results are persisted in table; otherwise, results
                    are garbage collected at the end of the session.
                    Default Value: False
                    Types: boolean

                volatile:
                    Optional Argument.
                    Specifies whether to put the results of the function in volatile table or not.
                    When set to True, results are stored in volatile table, otherwise not.
                    Default Value: False
                    Types: boolean

            Function allows the user to partition, hash, order or local order the input
            data. These generic arguments are available for each argument that accepts
            teradataml DataFrame as input and can be accessed as:
                * "<input_data_arg_name>_partition_column" accepts str or list of str (Strings)
                * "<input_data_arg_name>_hash_column" accepts str or list of str (Strings)
                * "<input_data_arg_name>_order_column" accepts str or list of str (Strings)
                * "local_order_<input_data_arg_name>" accepts boolean
            Note:
                These generic arguments are supported by teradataml if the underlying SQLE Engine
                function supports, else an exception is raised.


    RETURNS:
        Instance of ReadNOS.
        Output teradataml DataFrames can be accessed using attribute
        references, such as ReadNOS.<attribute_name>.
        Output teradataml DataFrame attribute name is:
            result


    RAISES:
        TeradataMlException, TypeError, ValueError


    EXAMPLES:
        # Notes:
        #    1. Get the connection to Vantage, before importing the function in user space.
        #    2. User can import the function, if it is available on the Vantage user is connected to.
        #    3. To check the list of analytic functions available on the Vantage user connected to,
        #       use "display_analytic_functions()".

        # Check the list of available analytic functions.
        display_analytic_functions()

        # Example 1: Reading PARQUET file from AWS S3 bucket.
        obj =  ReadNOS(location='/S3/s3.amazonaws.com/Your-Bucket/location/',
                       authorization='{"Access_ID": "YOUR-ID", "Access_Key": "YOUR-KEY"}',
                       stored_as='PARQUET')

        # print the result DataFame.
        print(obj.result)

        # Note: Before proceeding, verify with your database administrator that you have the correct privileges,
        # an authorization object, and a function mapping (for READ_NOS SQLE Engine function).
        # Below examples assume authorization object and location is stored in "READ_NOS_FM"
        # function mapping for READ_NOS SQL statement.

        # Example 2: Setting function mapping using configuration options.
        from teradataml.options.configure import configure
        configure.read_nos_function_mapping = "READ_NOS_FM"
        obj =  ReadNOS()

        # print the result DataFame.
        print(obj.result)

        # Example 3: Read PARQUET file in external storage with NOSREAD_KEYS Return Type.
        obj = ReadNOS(return_type="NOSREAD_KEYS")

        # print the result DataFame.
        print(obj.result)

        # Example 4 Read CSV file in external storage.
        obj = ReadNOS(location='/S3/s3.amazonaws.com/Your-Bucket/csv-location/',
                      stored_as='TEXTFILE')

        # print the result DataFame.
        print(obj.result)

        # Example 5 Read CSV file in external storage using "data" argument.
        # Create a table to store the data.
        con = create_context(host=host, user=user, password=password)
        con.execute("CREATE TABLE read_nos_support_tab (payload dataset storage format csv) NO PRIMARY INDEX;")
        read_nos_support_tab = DataFrame("read_nos_support_tab")

        # Read the CSV data using "data" argument.
        obj = ReadNOS(data=read_nos_support_tab,
                      location='/S3/s3.amazonaws.com/Your-Bucket/csv-location/',
                      stored_as='TEXTFILE')

        # print the result DataFame.
        print(obj.result)
    """